from gym.envs.registration import register

from bandit_env import multi_arm_bandit_gaussian_fixed
from bandit_env import multi_arm_bandit_gaussian_gaussian
from bandit_env import multi_arm_bandit_gaussian_uniform

environments = [['multi_arm_bandit_gaussian_fixed', 'v0'],
                ['multi_arm_bandit_gaussian_gaussian', 'v0'],
                ['multi_arm_bandit_gaussian_uniform', 'v0']]
for environment in environments:
    register(
        id='{}-{}'.format(environment[0], environment[1]),
        entry_point='gym_bandits:{}'.format(environment[0]),
        timestep_limit=1,
        nondeterministic=True,
    )
