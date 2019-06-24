# Introduction

The purpose of this projet is "play" with nba players stats by using different ML technique. This project is devided in 3 parts the first 2 are related. In the first part we will attempt to predict a player position on the court (PG, SG, SF, PF or C) based only on his stats. In the second part we will try to create our own new position by using clustering technique on the dataset. Finally in the last part, as said before not related to the others, we will try to find the best current player for the casting on the new Space Jam movie (more details in the dedicated chapter). 

# Dataset

As said in the introduction we use NBA player stats as our data. The dataset was found on the particular website : https://www.basketball-reference.com/. There is two type of player stats that we are interested in : 

- stats per game
- advanced stats

The first on, stats per game, is the more common on. Any NBA fan will know them. They mainly give informations about the players points, rebound and assists per game. We can also find the player shooting percentage, their fouls per game and other common data. 

The advance stats, as their name may tell, ar more in depth data. The will almost only speak to expert that are able to understand for example, a player defensive and offensive impact trough them. 

Both type of stats are stored in `csv` files. They each count around 700 entries but they will need a bit of pre-processing 

## Pre-processing




# ML tasks

As said in the introduction there is 3 main tasks in this projet. The following chapters will detail each on of them.  

## Position prediction

The purpose of the position prediction part of this project is to use Machine Learning to attempt to predict the position of a player based on his stats. 
Although every NBA fan will tell you that we are heading toward a "positionless" type of basketball is it possible to predict with respectable results the position of those players. 

In an attempt to have a better understanding of this subject the problem will be subdivided in 3 parts :

1. Using a TreeClassifier and regular stats per game
2. Using a TreeClassifier and advanced stats per game
3. Try to find the best classifier

The idea behind using a TreeClassifier in both part 1 and 2 is to be able to get a better understanding of the model "way of thinking". One of the great features a TreeClassifier allow us to use is that it is really easy to get 


## Clustering


## Space Jam


# Results

## Position prediction

## Clustering

## Space Jam

# Conclusion
