from gym.scoreboard.registration import add_task, add_group


add_group(
    id='bandits',
    name='Bandits',
    description='Various multi-armed Bandit environments'
)

add_task(
    id='multi_arm_bandit_gaussian_fixed-v0',
    group='bandits',
    experimental=True,
    contributor='bardofcodes',
    summary="multi-armed bandit mentioned with reward based on a Gaussian distribution",
    description="""
    Each bandit gives a fixed reward,'r', where 'r' is sampled from a Gaussian Distribution(5,2)
    """,
    background=""
)

add_task(
    id='multi_arm_bandit_gaussian_gaussian-v0',
    group='bandits',
    experimental=True,
    contributor='bardofcodes',
    summary="multi-armed bandit with each bandit having a normal distribution for reward distribution",
    description="""
     Each bandit has a N(r,1) reward distribution, where 'r' is sampled from a Normal(5,2) distribution.
    """,
    background=""
)

add_task(
    id='multi_arm_bandit_gaussian_uniform-v0',
    group='bandits',
    experimental=True,
    contributor='bardofcodes',
    summary="multi armed bandit, where each bandit has a uniform(n)*bernoulli(p) distribution",
    description="""
    Each bandit has a n*Bernoulli(p) reward distribution, 
    where 'p' is sampled from a uniform(0,1) distribution.
    and 'n' is sampled from normal(0,1) distribution
        """,
    background=""
)

