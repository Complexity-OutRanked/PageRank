# Determining whether Google really does have the best search engine algorithm
Katya Donovan and Young Seok Kim
## Abstract
In Page and Brin's paper *The PageRank Citation Ranking: Bringing Order to the Web*, the two Stanford researchers design a method which matches web pages objectively to determine a web user's interest in a website. The method ranks the websites based on the number of back links and links that the website has. We compare the PageRank algorithm with a method that determines the betweenness centrality, or the importance of nodes based on the shortest paths between different nodes. We use Brandes' optimized algorithim as described in *A Faster Algorithm for Betweenness Centrality* to verify that PageRank is a good factor to add to the Google search algorithm, by examining if there is high correlation between the probability distribution of page rank and the betweenness centrality of the nodes. We also compare the PageRank algorithm to a word frequency algorithm, mimicking earlier search algorithms in order to determine which one produces better results.

## PageRank
PageRank is an algorithm developed by Sergey Brin and Larry Page that is used by early Google Search to rank websites in their search engine results. Unlike other algorithms at that time, it does not use any content information other than the links. It uses the link information to construct a graph of websites, and determines the probability distribution of a user landing on each webpage.

## Replicating PageRank
Following *Google’s PageRank: The Math Behind the Search Engine*, we implement Google's PageRank algorithm. We verify that our replication is aligned with the paper's by using the data from the paper and checking that our results match the paper's results. Table 1 shows the results of the paper, and Table 2 shows our own results. Since the results are identical, we believe that our page rank algorithm matches the paper's.

![Table 1](/figures/paperResult.png "Table 1")
###### Table 1 : Results from *Google’s PageRank: The Math Behind the Search Engine*

![Table 2](/figures/ourResult.png "Table 2")
###### Table 2 : Results from our [own implementation](https://github.com/Complexity-OutRanked/PageRank/blob/master/code/PageRank.ipynb)

## Evaluating PageRank
One of the challenges of experimentation with PageRank is determining how to measure the accuracy of the PageRank system. With the probability distribution as an output, it is hard to evaluate the output result since searches are inherently subjective. Even in the original paper, the evaluation of the PageRank algorithm is omitted. We extend our project to further evaluate the PageRank model by comparing PageRank to betweenness centrality in order to evaluate the probability values of the nodes. 

### Betweenness centrality
Betweenness centrality or *betweenness* is a good measure to evaluate the *importance* of nodes. Formally, betweenness is defined as follows,
> **Betweenness** centrality quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.

Mathematically, centrality is defined as

<img src="/figures/BetweennessEquation.png" width="300" height="100" />

where <img src="/figures/sigma_st.png" width="40" height="20" /> is the total number of shortest paths from node s to node t and <img src="/figures/sigma_st(v).png" width="50" height="20" /> is the number of those paths that pass through v.

### Evaluating with synthetic random graph
For the experiments, we assume that if there is a high correlation between the betweenness value and the PageRank probability of each node, we would conclude that the algorithm worked accurately to evaluate each node. Figure 1 and 2 show the correlation between betweenness value and the PageRank probability on Barabási–Albert graph and Erdős–Rényi graph, respectively. 

A Barabasi-Albert has central nodes with many edges, so we expect to see a correlation between the two over a large range of values. As shown in Figure 1, there is a high correlation between the PageRank probability of each node and the betweenness centrality. As expected, there are less nodes that have a high PageRank and betweenness centrality value than nodes that have a low page rank, because Barabasi-Albert graphs have few central nodes. Figure 2 depicts the probability based on the PageRank algorithm against the betweenness centrality for an Erdos-Renyi model, which also has a strong correlation. Since an Erdős–Rényi model is a random graph, the correlation follows a normal distribution, with many nodes having an average betweenness and PageRank probability and a few having a low and high PageRank probability and betweenness. Since there is a strong correlation between PageRank probability and centrality, we believe that 
PageRank is an effective metric of determining the importance of nodes.


![Figure 1](/figures/BA1000.png "Figure 1") 
###### Figure 1: Comparing PageRank and Betweenness Centrality for BA graph with 1000 nodes and 300 edges

![Figure 2](/figures/ER1000.png "Figure 2")
###### Figure 2: Comparing PageRank and Betweenness Centrality for ER graph with 1000 nodes and p=0.3

### Evaluating with real world dataset
 
Figure 3 shows the correlation for *Wikispeedia navigation paths* graph from SNAP. “Wikispeedia” dataset is a search path where users are asked to navigate from a given source article to a target article, by only clicking Wikipedia links. We thought this task is relevant because it gives the data of pages that are linked to each other. 
 
![Figure 3](/figures/Wikispeedia.png "Figure 3")
###### Figure 3: Comparing PageRank and Betweenness Centrality for Wikispeedia dataset
 
 
## Comparing Search Engines
Although search engine algorithms are much more complex now, in the beginning the most basic search algorithms matched up a user's web search with pages with the highest word frequency. JumpStation, an early search engine algorithm, indexed through the website titles and listed the web pages with the most common words. On a smaller scale, we compare our word frequency algorithm with or without the PageRank algorithm. Our implementation of the word frequency algorithm consists of finding the hundred top articles from our database with the highest count of the searched word. We create a new graph with only these websites and use Page Rank to determine the top ten web pages. We compare the results from the word frequency algorithm with and without the PageRank algorithm in Table 3. Table 3 shows the top three Wikipedia pages for each algorithm.


| Word  | PageRank  | Word Count  | 
|---|---|---|
|  Mathmatics |  Georg Cantor, Algebra, E.P. Wigner |  Mathematics, Applied Mathematics, David Hilbert |
|  Marx | Marxism, Anarchism, Sociology  |  Karl Marx, Marxism, Communism |
|  Hinduism |  History of Buddhism, United Kingdom, Max Weber |  Hinduism, Religion, Indonesia |
|  Atheirm |  Atheism, Deity, Eliminative materialism |  Atheism, Thomas Hobbes, Humanism |

###### Table 3: Comparing Page Rank and Word Frequency Algorithms

Table 3 shows that the different algorithms will produce different results, but determining which one is more accurate is difficult, because it is subjective to the user Additonally, the data is a subset of the wikipedia data and only one word was inputted for the web search, making the model less representative of the actual process. For most words, the word frequency algorithm without PageRank will rank the Wikipedia page of that searched word as the top page. However, the PageRank algorithm ranks Wikipedia pages that a user might be interested in, even if the searched word is not exactly the same. 

One of the reasons that the PageRank algorithm might not work well in this scenario is because of the dataset. Wikipedia is very structured, having webpages dedicated to simply one word, which is why the word frequency algorithm would work very well. Additionally, all of Wikipedia will have reliable information, since it is all part of the same larger web page. For the world wide web as a whole, PageRank will most likely produce more accurate results because it can rank pages based on their popularity, which word frequency neglects. Additionally, most web pages are not centered around a certain word, but rather around a certain topic or idea, which makes word frequency more difficult. However, based on our results, we conclude that for a small portion of Wikipedia, a search result with only the word for the desire Wikipedia page is better than the PageRank algorithm combined with the word frequency algorithm.
 
## Bibliography

#### Bibliography 1

Page, Lawrence and Brin, Sergey and Motwani, Rajeev and Winograd, Terry (1999) The PageRank Citation Ranking: Bringing Order to the Web. Technical Report. Stanford InfoLab.

Page and Brin design a method known as PageRank, which matches web pages objectively in order to calculate a person's interest in them. By modeling each of the website's as nodes and using links as edges, they created an algorithm that determines the rank of website based on how many websites link to them, taking the popularity of the websites that link to them into consideration. Page and Brin tested their model by comparing the predictions for future citation counts on the Stanford web against the citation counts and found that Pagerank was a better predictor.

#### Bibliography 2

Rogers, I. (2005, May 7). The Google Pagerank Algorithm and How it Works. Retrieved October 1, 2017, from http://www.alvit.de/vf/en/web-development-the-google-pagerank-algorithm-and-how-it-works.html

Rogers explains the Google PageRank algorithm by simulating how PageRank is determined using small systems. PageRank determines how important a page is by using how many links from other pages go to the page, and how many links it gives to other websites. Although Rogers did not design his own model, he used a previous algorithm on a smaller network in order to better explain page rank.

#### Bibliography 3

Wills, R. (2006, May 1). *Google's PageRank: The math behind the search engine.* Raleigh, NC

This paper reviews mathematics behind the PageRank algorithm. The paper introduces some backgrounds on the Google’s search engine first, and explains details on the mathematics behind the PageRank. It also points out a *dangling node* problem and suggests a potential fix for the problem. After that, it also introduces a *personalization vector* and talks about the algorithm which computes the PageRank score. Overall, this paper concisely defines the mathematical problem for the PageRank, and gives us simple explanation over some of the details in the PageRank. I think this paper will be very useful to design the experiments.

#### Bibliography 4

Langville, A.M. and Meyer, C.D. (2004, October 20). *Deeper inside PageRank.* Intenet Math.

This paper talks about further details on PageRank algorithm. The first two sections talk about the background on PageRank, and the third section explains the general concept of the algorithm. Then, in section 4, it introduces storage issues on PageRank algorithm and explains different approaches on how to resolve the storage issue. In section 5, the paper gives detailed mathematics on solving the PageRank problem. After that, it gives some intuitions about the alpha value and personalization vector and etc… Overall, this paper goes quite deep into the algorithm and gives more perspective on the PageRank algorithm.

#### Bibliography 5

Brandes, U. (2001). *A Faster algorithm for betweenness centrality.* Journal of Mathematical Sociology. 25. 163-177.

Brandes designs a less computational intensive method to determine the betweenness centrality of nodes in a given graph. Betweenness centrality is the measure of the most important nodes in a graph based on the shortest paths. Brandes was able to reduce the O(n^3) time to O(nm), where m is the number of links and n is the number of nodes. Reducing the computation of calculating betweenness centrality makes analyzing social networks much easier.
