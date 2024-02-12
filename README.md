# Beta Distribution for Ad Prediction -- a typical thompson bandit solution

## overall introduction
This program is a solution for bandit problem by using Thompson method.

The Multi-Armed Bandit problem is the simplest setting of reinforcement learning. Suppose that a gambler faces a row of slot machines (bandits) on a casino. Each one of the K machines has a probability θk of providing a reward to the player. Thus, the player has to decide which machines to play, how many times to play each machine and in which order to play them, in order to maximize his long-term cumulative reward.
At each round, we receive a binary reward, taken from an Bernoulli experiment with parameter θk. Thus, at each round, each bandit behaves like a random variable Yk∼Bernoulli(θk). This version of the Multi-Armed Bandit is also called the Binomial bandit.

In ad prediction, bandit is a typical module for choosing an ad with the highest probability to be clicked. 

A python beta distribution is adopted for establishing the parameter sets for each customer group. Once we have the customer group id, we can accordingly recommend the most highly-probable ad for the user.

## Thompson multi-arm bandit algorithm explanation
A [Thompson tutorial](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf) provided by Stanford University has below conclusion.
For K actions, mean rewards $\theta = \left(\theta_a, \dots, \theta_K\right)$ is unknown. 
A reward $r_1 \in [0, 1]$ is generated with success probability $$\mathbb P\left(r_1 = 1 | x_1, \theta\right) = \theta_{x_1}$$ After observing $r_1$, system will update its parameters accordingly.

## Algorithm
> for t = 1, 2, $\dots$ do 
> > \# sample model:\
> > for k = 1, $\dots$ , K do
> > > sample $\hat \theta_k \sim beta \left(\alpha_k, \beta_k\right)$ 
> > 
> > end for 
>  
> > \# select and apply action: \
> > $x_t \leftarrow argmax_k \hat \theta_k$
> >
> > \# update distribution: \
> > $(\alpha_{x_t}, \beta_{x_t})\leftarrow(\alpha_{x_t} + r_t, \beta_{x_t} + 1 - r_t)$ 
>
> end for 


## Input data explanation
In the data folder, two sample csv are provided. 
1. Segments.csv contains 
- user id 
- its segment id. 
2. Summary.csv contains 
- user id
- ad id
- ad total number of display 
- clicks of the ad