
import numpy as np
## Multi Bandit Class
class multi_arm_bandit():

	def __init__(self,bandit_list=[]):
		self.bandit_list = bandit_list


	@classmethod
	def template(cls,n_bandits,bandit_func_list,bandit_params_list):
		bandit_list = []
		for i in range(n_bandits):
			bandit_list.append(bandit(bandit_func_list[i],bandit_params_list[i]))
		multi_bandit = cls(bandit_list)
		return multi_bandit

	@classmethod
	def distribution(cls,n_bandits,dist_func_and_args_list,bandit_dist_func):
		multi_params_list = []
		for i in range(n_bandits):
			params_list = []
			for j in dist_func_and_args_list:
				params_list.append(j[0](*j[1]))
			multi_params_list.append(params_list)
		if not type(bandit_dist_func) is list:
			bandit_dist_func = [bandit_dist_func,]*n_bandits
		multi_bandit = cls().template(n_bandits,bandit_dist_func,multi_params_list)
		return multi_bandit

	@classmethod
	def gaussian(cls,n_bandits,mean_reward,std_reward,bandit_param_2_list=1,bandit_func = np.random.normal):
		if not type(bandit_param_2_list) is list:
			bandit_param_2_list = [bandit_param_2_list,]*n_bandits
		if len(bandit_param_2_list)<n_bandits:
			multi_bandit = cls().distribution(n_bandits,[(np.random.normal,[mean_reward,std_reward]),
				(np.random.choice,[bandit_param_2_list,None,False])],bandit_func)
		else:
			params_list = []
			for i in range(n_bandits):
				params = [np.random.normal(mean_reward,std_reward), bandit_param_2_list[i]]
				params_list.append(params)
			multi_bandit = cls().template(n_bandits,[bandit_func,]*n_bandits,params_list)
		return multi_bandit
	
	@classmethod
	def gaussian_fixed(cls,n_bandits,mean_reward,std_reward):
		params_list = np.random.normal(mean_reward,std_reward,n_bandits)
		params_list = [[[i],None]for i in params_list]
		multi_bandit = cls().template(n_bandits,[np.random.choice,]*n_bandits,params_list)
		return multi_bandit

	def get_reward(self,action):
		return self.bandit_list[action].get_reward()





# Single Bandit Class
class bandit():

	def __init__(self,draw_func = None,params=None):
		'''
		This defines our bandit. The bandit when triggered will output a reward from its reward distribution.
		Bandit has two parameters
		:draw_func: The numpy function specifying the reward distribution.
		:params: The parameters of the draw function.

		'''
		self.draw_func = draw_func
		self.params = params

	@classmethod
	def uniform(cls,lower,upper):
		bandit = cls(np.random.uniform,[lower,upper])
		return bandit

	@classmethod
	def normal(cls, mean,std):
		bandit = cls(np.random.normal,[mean,std])
		return bandit

	@classmethod
	def multi_value(cls,val_list,prob_list = [1]):
		bandit = cls(np.random.choice,[val_list,None,prob_list])
		return bandit

	def get_reward(self):
		'''
		When Trigged, the bandit draws a sample from its reward distribution and returns it.
		'''
		reward = self.draw_func(*self.params)
		return reward
	