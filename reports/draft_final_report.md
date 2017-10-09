# Determining whether Google really does have the best search engine algorithm
Katya Donovan and Young Seok Kim
### Abstract
In Page and Brin's paper *The PageRank Citation Ranking: Bringing Order to the Web*, the two Stanford researchers design a method which matches web pages objectively to calculate a web user's interest in a website. The method ranks the websites based on the number of back links and links that the website has. In Brandes' paper *A Faster Algorithm for Betweenness Centrality*, Brandes explores a method to calculate the centrality of nodes based on the shortest paths between different nodes. We compared the two methods of determining a website's popularity to determine whether PageRank is superior.

### Bibliography

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

#### Bibliography %
