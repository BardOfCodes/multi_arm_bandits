# Bandit Environments

Multiple instances of n-armed bandit environments for the OpenAI Gym

## Modular Construct

This env is made on top of `multi_arm_bandit` class, which contains a list of `bandit` object. 

### Bandit
Each `bandit` has two core variables:
* `draw_func` : This is the function that the bandit uses for drawing the reward.
* `params` : This is the parameters that the bandit uses for drawing the reward.

Some simple bandits initialization methods have been added. For eg:
```
bandit_1 = bandit().uniform(0,1)
# bandit 1 is a bandit which finds its reward from a [0,1] uniform distribution.

bandit_2 = bandit().normal(0,1)
# bandit_2  is a bandit which finds its reward from a Normal(0,1) distribution.
```
### Multi-arm-Bandit
Each  `multi_arm_bandit` contains a list of `bandits` from which it recieves rewards based on which bandit was selected in the action.<br>

Useful information
*`bandit_list` :  Contains a list in which each element is a `bandit` instance. 
*`get_reward` : Function which takes bandit index as input and returns the reward from the selected bandit.

Some simple `multi_arm_bandit` initialization methods have been added. For eg:
```
multi_arm_bandits_1 = multi_arm_bandits().gaussian(10,5,2,1)
# constructs a multi_arm_bandit, with 10 arms, each having a N(r,1) reward distribution, where 'r' is sampled from a Normal(5,2) distribution.

multi_arm_bandits_2 = multi_arm_bandits().gaussian_fixed(10,5,2)
# constructs a multi_arm_bandit, with 10 arms, each having a fixed reward 'r', where 'r' is sampled from a Normal(5,2) distribution.

```

This will help in forming various kinds of bandits and multi-arm bandit problems.


## Environments

* multi_arm_bandit_gaussian_fixed-v0: 10 armed bandit with fixed payouts from a gaussian distribution.

* multi_arm_bandit_gaussian_gaussian-v0: 10 armed bandit with that always pays out with a reward selected from a uniform distribution

* multi_arm_bandit_gaussian_uniform-v0: 10 armed bandit with each bandit giving reward from a bernoilli distribution, and the reward values are alloted from a uniform distribution(Just to show the variations possible :D).

### Installation
```
git clone git@github.com:bardofcodes/multi_arm_bandits.git
cd multi_arm_bandits
pip install -e .
```

In your gym environment
```
import gym_bandits
env = gym.make("BanditTenArmedGaussian-v0") # Replace with relevant env
```

## Future work
* Check integration with OpenAI gym.
* Try to make variable parameter environment in gym.

## Acknowledgement

* Based on the work of [JKcooper2](https://github.com/JKCooper2/gym-bandits/tree/67cb5a34a64be46da2853441dd2377f6853d0854). This repository is just a more extensively modifiable version of his code.