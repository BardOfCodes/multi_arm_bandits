import numpy as np

# gym module on top
import gym
from gym import spaces
from gym.utils import seeding
from multi_arm_bandit import *

class bandit_env(gym.Env):
    """
    Bandit environment base to allow agents to interact with the class n-armed bandit
    in different variations
    p_dist:
        A list of probabilities of the likelihood that a particular bandit will pay out
    r_dist:
        A list of either rewards (if number) or means and standard deviations (if list)
        of the payout that bandit has
    """
    def __init__(self, multi_arm_bandit):

        self.multi_arm_bandit = multi_arm_bandit
        self.n_bandits = len(multi_arm_bandit.bandit_list)
        self.action_space = spaces.Discrete(self.n_bandits)
        self.observation_space = spaces.Discrete(1)
        self._seed()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action)

        reward = 0
        done = True

       	reward = multi_arm_bandit.trigger

        return 0, reward, done, {}

    def _reset(self):
        return 0

    def _render(self, mode='human', close=False):
        pass

class multi_arm_bandit_gaussian_fixed(bandit_env):
	# constructs a multi_arm_bandit, with n_bandits arms, each having a fixed reward 'r', 
	# where 'r' is sampled from a Normal(reward_mean,reward_std) distribution.
	def __init__(self,n_bandits = 10,reward_mean = 5,reward_std = 2):
		multi_arm_bandit = multi_arm_bandit().gaussian_fixed(n_bandits,reward_mean,reward_std)
		bandit_env.__init__(self,multi_arm_bandit)

class multi_arm_bandit_gaussian_gaussian(bandit_env):
	# constructs a multi_arm_bandit, with 10 arms, each having a N(r,1) reward distribution, 
	# where 'r' is sampled from a Normal(5,2) distribution.
	def __init__(self,n_bandits = 10,reward_mean = 5,reward_std = 2,bandit_std=1):
		multi_arm_bandit = multi_arm_bandits().gaussian(n_bandits,reward_mean,reward_std,bandit_std)
		bandit_env.__init__(self, multi_arm_bandit)

class multi_arm_bandit_gaussian_uniform(bandit_env):
	# constructs a multi_arm_bandit, with n_bandit arms, each having a n*Bernoulli(p) reward distribution, 
	# where 'p' is sampled from a uniform(0,1) distribution.
	# and 'n' is sampled from normal(0,1) distribution
	def __init__(self,n_bandit=10,n_mean=1,n_std=1):
		bandit_list = []
		for i in range(n_bandit):
			n = np.random.normal(n_mean,n_std)
			bandit_list.append(bandit(np.random.choice,[[0,],None,[1-p,p]]))
		multi_arm_bandit = multi_arm_bandit(bandit_list)
		bandit_env.__init__(self, multi_arm_bandit)

