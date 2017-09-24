

During our project, we will explore the Google PageRank algorithm by designing a model based on it. Focusing on only a subset of Wikipedia pages, we will make a small-scale model, using wikipedia pages as the nodes, and the links to other pages as the edges. By designing this model, we will be able to understand how the popularity of webpages are affected by their backlinks from other pages. 

As we approach this project, we first plan to replicate a small model of Google's PageRank, using a limited number of nodes and edges. PageRank assigns each website a rank, which is then used to help order search results. We will determine this rank by examining the links of going to each page, which give the page a higher rank in proportion to how highly ranked those websites are. 

As we move forward on this project, we could extend it farther. We could model a larger network of pages, which means that would have to account for a large amount of data. 

4) Present 1-3 experiments from these papers that you plan to replicate and 1-3 extensions or variations of those experiments you are considering.

We will display our results in a graph that changes the size of each node depending on its page rank. That way we will have a clear visualization of which nodes have the highest rank and which ones do not. This will allow us to preliminary check our model to see if the pages with the most backlinks have the highest page ranks.

To validate our model, we will compare our results to the Wikipedia’s Pageviews Analysis, in order to determine whether there is a slight correlation between our PageRank results and the popularity of the Wikipedia pages. However, since we are only modeling a small subset of the Wikipedia pages, there will most likely still be many discrepancies between the two, as we would not have accounted for any links connecting to our nodes that do not come from one of ours model’s nodes. 

As we start this project, we are concerned that data retrieval may be difficult. Our model depends on the links of wikipedia page articles, which might be fairly difficult to scrape, since the data might not be public. Furthermore, we are worried about how to validate our model. As we are only modeling a small part of the world wide web, it might be difficult to compare our results against Google’s actual PageRank algorithm, as we will have neglected many links in our model. Additionally, scaling our model up would be difficult, as optimizing the processing of large data sets can be challenging.

8) Outline next steps.  For each team member, what do you plan to work on immediately?  For the team, what do you think you can get done in the first week?  Consider using Trello (or a similar tool) to delegate and track tasks.

# Bibliography

## Bibliography 1
[The PageRank Citation Ranking: Bringing Order to the Web](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

*Page, Lawrence and Brin, Sergey and Motwani, Rajeev and Winograd, Terry (1999). Technical Report. Stanford InfoLab*

Page and Brin design a method known as PageRank, which matches web pages objectively in order to calculate a person's interest in them. By modeling each of the website's as nodes, and using links as edges, they created an algorithm that determines the rank of website based on how many websites link to them, taking the popularity of the websites that link to them into consideration. Page and Brin tested their model by comparing the predictions for future citation counts on the Stanford web against the citation counts and found that Pagerank was a better predictor. 

## Bibliography 2
[The Google Pagerank Algorithm and How It Works](http://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm)

*Rogers, Ian. IPR Computing Ltd.*

Rogers explains the Google PageRank algorithm by simulating how PageRank is determined using small systems. PageRank determines how important a page is by using how many links from other pages go to the page, and how many links it gives to other websites. Although Rogers did not design his own model, he used a previous algorithm on a smaller network in order to better explain page rank.

## Bibliography 3
[Google’s PageRank: The Math Behind the Search Engine](http://www.cems.uvm.edu/~tlakoba/AppliedUGMath/other_Google/Wills.pdf)

*Rebecca S. Wills*

This paper reviews mathematics behind the PageRank algorithm. The paper introduces some backgrounds on the Google’s search engine first, and explains details on the mathematics behind the PageRank. It also points out a *dangling node* problem and suggests a potential fix for the problem. After that, it also introduces a *personalization vector* and talks about the algorithm which computes the PageRank score. Overall, this paper concisely defines the mathematical problem for the PageRank, and gives us simple explanation over some of the details in the PageRank. I think this paper will be very useful to design the experiments.

## Bibliography 4
[Deeper Inside PageRank](http://meyer.math.ncsu.edu/Meyer/PS_Files/DeeperInsidePR.pdf)

*Amy N. Langville and Carl D. Meyer*

This paper talks about further details on PageRank algorithm. First two sections talk about the background on PageRank, and the third section explains the general concept of the algorithm. Then, in section 4, it introduces storage issues on PageRank algorithm and explains different approaches on how to resolve the storage issue. In section 5, the paper gives detailed mathematics on solving the PageRank problem. After that, it gives some intuitions about the alpha value and personalization vector and etc… Overall, this paper goes quite deep into the algorithm and gives more perspective on the PageRank algorithm.

