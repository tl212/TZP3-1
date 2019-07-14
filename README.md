## TZP3-1 | Hybrid Movie Recommender System - Part 1 
### Overview 

In this project we are going to implement two of the most popular recommender engines; Content-Based Filtering &  Collaborative Filtering. 

#### Content-Based Filtering

In a content-based filtering, the similarity between different products is calculated on the basis of the attributes of the products. For instance, in a content-based movie recommender system, the similarity between the movies is calculated on the basis of genres, the actors in the movie, the director of the movie, etc.

#### Collaborative Filtering

Collaborative filtering leverages the power of the crowd. The intuition behind collaborative filtering is that if a user A likes products X and Y, and if another user B likes product X, there is a fair bit of chance that he will like the product Y as well.

In this work we propose hybrid both engines; user-item interaction data and their contextual information.

Hybrid recommenders use both user-item interaction data and their contextual information. In this work, we propose new hybrid recommender algorithms by considering the relationship between content features. This relationship is embedded into the hybrid recommenders to improve their accuracy. We first introduce a novel method to extract the content feature relationship matrix, and then the collaborative filtering recommender is modified such that this relationship matrix can be effectively integrated within the algorithm. The proposed algorithm can better deal with the cold-start problem than the state-of-art algorithms. We also propose a novel content-based hybrid recommender system. Our experiments on a benchmark movie dataset show that the proposed approach significantly improves the accuracy of the system, while resulting in satisfactory performance in terms of novelty and diversity of the recommendation lists.
