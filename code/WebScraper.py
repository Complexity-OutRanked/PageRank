import sqlite3
import argparse
import time
import threading
import queue
import requests
from bs4 import BeautifulSoup

# Printer Lock
printer_lock = threading.Lock()

# Work Queue
job_queue = queue.Queue()

# for BFS
seen = set()

# Database related
db = sqlite3.connect('testdb.sqlite')
c = db.cursor()

# Create table for the graph data
try:
    c.execute('CREATE TABLE EDGES (source TEXT, destination TEXT)')
except:
    print("Database table already exists!")


# Function to add to db
def add_edge(s, d):
    try:
        c.execute("INSERT INTO EDGES (source, destination) VALUES ('{}', '{}')".format(s, d))
    except:
        print("Error occured while adding edges to the database")



# I am assuming site is like a following format
# /wiki/Alphabet
def scrape(site):
    sp = site.split('/') # [wiki, Alphabet]
    a = requests.get('https://en.wikipedia.org/wiki/Special:WhatLinksHere/{}?&limit=1000000&from=0'.format(sp[1]))
    b = BeautifulSoup(a.text, 'html.parser')
    c = b.find(id="mw-whatlinkshere-list")
    d = c.find_all('li')
    e = map(lambda elem:elem.a.get('href'), d)
    f = list(filter(lambda x: ':' not in x, e))
    return f




def lock_print(*args, **kwargs):
    with printer_lock:
        print(*args, **kwargs)


def worker(i):
    lock_print("Worker {} is starting...".format(i))
    # Setup

    # Run
    try:
        while True:
            job = job_queue.get(block=False)
            lock_print("Worker {} is working on {}".format(i, job))
            lock_print("There are now {} jobs in the queue".format(job_queue.qsize()))
            # Work
            sites = scrape(job)
            # Add to db
            for site in sites:
                add_edge(site, job)

            # Print information
            lock_print("{} had {} many backlinks!".format(job, len(sites))

            # Add more work to the queue
            new_sites = set(new_sites) - seen
            for site in new_sites:
                job_queue.put(site)

            job_queue.task_done()
            #time.sleep(1)
    except queue.Empty:
        with printer_lock:
            print("Queue is now empty!")
            print("Worker {} is done.".format(i))

def main(args):

    # Insert jobs to the queue
    job_queue.put('/wiki/Alphabet')

    # Spawn threads
    number_of_threads = args.threads
    worker_threads = []
    try:
        for i in range(number_of_threads):
            t = threading.Thread(target=worker, args=[i])
            worker_threads.append(t)
            t.start()
        for t in worker_threads:
            t.join()
    except KeyboardInterrupt:


    print("Work is all done")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--threads', type=int, default=4, help='number of threads to run')
    args = parser.parse_args()

    main(args)
