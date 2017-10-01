import scrapy


class QuotesSpider(scrapy.Spider):
    name = "webcrawler"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Special:WhatLinksHere/Alphabet'
            ]
        self.target_list=[]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.append_nodes)



    def parse(self, response):
        body = response.css("div.mw-body")
        self.content = body.css("div.mw-body-content")
        for span in self.content.css("span.mw-whatlinkshere-tools").extract():
            title = span.split("target=")
            target = title[1].split('" title')
            yield target[0]
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page"""

    def link_next_page(self,response):
        ul = self.content.xpath("//div[@id='mw-content-text']/hr")
        self.li = ul.xpath("//ul[@id='mw-whatlinkshere-list']")
        next_50 = self.li.xpath("//a[text()='next 50']/@href").extract()
        if next_50 != []:
            yield response.follow(next_50[0], callback=self.append_nodes)
        else:
            return self.target_list

    def append_nodes(self,response):
        for i in self.parse(response):
            self.target_list.append(i)
        #print(self.target_list)
        return self.link_next_page(response)


"""    def find_nodes(self,response):
        for i in self.parse(response):
            self.target_list.append(i)
        print(self.target_list)
        return self.target_list
        #link_next_page(response)


    def save(self,response):
        find_nodes()



        #target_list.append(i)

    def link_backlink(self,response):
        self.content = body.css("div.mw-body-content")
        ul = self.content.xpath("//div[@id='mw-content-text']/hr")
        li = ul.xpath("//ul[@id='mw-whatlinkshere-list']")
        for href in li.xpath("//li//a").extract():"""
