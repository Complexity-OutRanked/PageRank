# Determining whether Google really does have the best search engine algorithm
Katya Donovan and Young Seok Kim
## Abstract
In Page and Brin's paper *The PageRank Citation Ranking: Bringing Order to the Web*, the two Stanford researchers design a method which matches web pages objectively to determine a web user's interest in a website. The method ranks the websites based on the number of back links and links that the website has. We compared the PageRank algorithm with a method that determines the betweenness centrality, or the importance of nodes based on the shortest paths between different nodes. We used Brandes' optimized algorithim as described in *A Faster Algorithm for Betweenness Centrality* to verify that page rank was a good factor to add to the google search algorithm, by examining if there was high correlation between the probability distribution of page rank and the betweenness centrality of the nodes. Once we checked PageRank, we implemented it on a collaboration network to compare each node's betweenness centrality. 

## Verifying PageRank
Following *Google’s PageRank: The Math Behind the Search Engine*, we implemented Google's Page Rank algorithm. We verified that our replication was aligned with the paper's by using the same data matrices as the paper and checking that our results matched the paper's. The following table shows the results of the paper, and the table after that show our own results. The results are very similar, which allowed us to believe that our page rank algorithm matched the paper's.
![Figure 1](/figures/paperResult.png "Figure 1")
![Figure 1](/figures/ourResult.png "Figure 1")

In order to determine whether PageRank would accurately calculate the websites that the viewer is most interested in, we decided to compare it against a metric for determining the centrality of nodes in a graph based on shortest path lengths, known as *betweenness centrality*. We assumed that if there was a high correlation between the page rank probability distribution of a node and the betweenness centrality of the same node, then the page rank algorithm would be an accurate way of determining which websites are most popular. The first figure depicts each node with its corresponding page rank probability and betweeness centrality for a Barabasi-Albert graph. A Barabasi-Albert has central nodes with many edges, so we expected to see a  correlation between the two over a large range of values. As shown in the first figure, there is a high correlation between the page rank probability of each node and the betweenness centrality. As expected, there are less nodes a that have a high page rank and betweenness centrality value than nodes that have a low page rank, because Barabasi-Albert graphs have few central nodes. The second figure depicts the probability based on the page rank algorithm against the betweenness centrality for a Erdos-Renyi model, which also has a strong correlation. Since an Erdos-Renyi model is a random graph, the correlation would follow a normal distribution, with many nodes having an average betweenness and page rank probability and a few having a low and high page rank probability and betweenness. We believe that the page rank algorithm would be a good metric to determine which websites should be shown first, since there is a strong correlation between page rank probability and centrality. 

![Figure 1](/figures/BA1000.png "Figure 1")  ![Figure 2](/figures/ER1000.png "Figure 2")

## Determining Highest Rank
Since we verified that the page rank algorithm worked, we calculated the page rank of collaboration network in order to determine which websites in the network had the highest probability of being chosen, and thus which ones would show up earlier in a google search. The third shows the graph of the collaboration network comparing the betweenness and the page rank probability. Unlike the other two figures, there is a smaller correlation between the probability output from page rank and the betweenness centrality. We have determined that this is most likely caused by a variety of nodes in the network that have a large range of edges but do not act as a central hub, diminishing their betweenness centrality while increasing their page rank. The PageRank algorithm is able to account for the nodes with many edges that are not part of the shortest path for many nodes. 


![Figure 3](/figures/CollaborationNetwork.png "Figure 3")

| Word  | PageRank  | Word Count  | 
|---|---|---|
|  Mathmatics |  Georg Cantor, Algebra, E.P. Wigner |  Mathematics, Applied Mathematics, David Hilbert |
|  Marx | Marxism, Anarchism, Sociology  |  Karl Marx, Marxism, Communism |
|  Hinduism |  History of Buddhism, United Kingdom, Max Weber |  Hinduism, Religion, Indonesia |
|  Atheirm |  Atheism, Deity, Eliminative materialism |  Atheism, Thomas Hobbes, Humanism |



## Bibliography

#### Bibliography 1
[The PageRank Citation Ranking: Bringing Order to the Web](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

*Page, Lawrence and Brin, Sergey and Motwani, Rajeev and Winograd, Terry (1999). Technical Report. Stanford InfoLab*

Page and Brin design a method known as PageRank, which matches web pages objectively in order to calculate a person's interest in them. By modeling each of the website's as nodes, and using links as edges, they created an algorithm that determines the rank of website based on how many websites link to them, taking the popularity of the websites that link to them into consideration. Page and Brin tested their model by comparing the predictions for future citation counts on the Stanford web against the citation counts and found that Pagerank was a better predictor.

#### Bibliography 2
[The Google Pagerank Algorithm and How It Works](http://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm)

*Rogers, Ian. IPR Computing Ltd.*

Rogers explains the Google PageRank algorithm by simulating how PageRank is determined using small systems. PageRank determines how important a page is by using how many links from other pages go to the page, and how many links it gives to other websites. Although Rogers did not design his own model, he used a previous algorithm on a smaller network in order to better explain page rank.

#### Bibliography 3
[Google’s PageRank: The Math Behind the Search Engine](http://www.cems.uvm.edu/~tlakoba/AppliedUGMath/other_Google/Wills.pdf)

*Rebecca S. Wills*

This paper reviews mathematics behind the PageRank algorithm. The paper introduces some backgrounds on the Google’s search engine first, and explains details on the mathematics behind the PageRank. It also points out a *dangling node* problem and suggests a potential fix for the problem. After that, it also introduces a *personalization vector* and talks about the algorithm which computes the PageRank score. Overall, this paper concisely defines the mathematical problem for the PageRank, and gives us simple explanation over some of the details in the PageRank. I think this paper will be very useful to design the experiments.

#### Bibliography 4
[Deeper Inside PageRank](http://meyer.math.ncsu.edu/Meyer/PS_Files/DeeperInsidePR.pdf)

*Amy N. Langville and Carl D. Meyer*

This paper talks about further details on PageRank algorithm. First two sections talk about the background on PageRank, and the third section explains the general concept of the algorithm. Then, in section 4, it introduces storage issues on PageRank algorithm and explains different approaches on how to resolve the storage issue. In section 5, the paper gives detailed mathematics on solving the PageRank problem. After that, it gives some intuitions about the alpha value and personalization vector and etc… Overall, this paper goes quite deep into the algorithm and gives more perspective on the PageRank algorithm.

#### Bibliography 5
[A Faster Algorithm for Betweenness Centrality](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.2024&rep=rep1&type=pdf)

*Ulrik Brandes*

Brandes designs a less computational intensive method to determine the betweenness centrality of nodes in a given graph. Betweenness centrality is the measure of the most important nodes in a graph based on the shortest paths. Brandes was able to reduce the O(n^3) time to O(nm), where m is the number of links and n is the number of nodes. Reducing the computation of calculating betweenness centrality makes analyzing social networks much easier.
