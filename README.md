# Beta Distribution for Ad Prediction -- a typical thompson bandit solution

## overall introduction
This program is a solution for bandit problem by using Thompson method.

The Multi-Armed Bandit problem is the simplest setting of reinforcement learning. Suppose that a gambler faces a row of slot machines (bandits) on a casino. Each one of the K machines has a probability θk of providing a reward to the player. Thus, the player has to decide which machines to play, how many times to play each machine and in which order to play them, in order to maximize his long-term cumulative reward.
At each round, we receive a binary reward, taken from an Bernoulli experiment with parameter θk. Thus, at each round, each bandit behaves like a random variable Yk∼Bernoulli(θk). This version of the Multi-Armed Bandit is also called the Binomial bandit.

In ad prediction, bandit is a typical module for choosing an ad with the highest probability to be clicked. 

A python beta distribution is adopted for establishing the parameter sets for each customer group. Once we have the customer group id, we can accordingly recommend the most highly-probable ad for the user.

## Input data explanation
In the data folder, two sample csv are provided. 
Segments.csv contains 
    -user id 
    -its segment id.
summary.csv contains
    -user id
    -ad id
    -ad total number of display
    -clicks of the ad