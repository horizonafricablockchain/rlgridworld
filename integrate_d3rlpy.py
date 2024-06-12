import numpy as np
from rlgridworld.gridenv import GridEnv
import d3rlpy
from d3rlpy.algos import DQN
from d3rlpy.datasets import MDPDataset
from d3rlpy.preprocessing import Scaler,ActionScaler

# Set up the environment
env = GridEnv(load_chars_rep_fromd_dir='EnvSettings/SimpleTarget.txt')

# Set up d3rlpy components
scaler = Scaler('min_max')
action_scaler = ActionScaler('min_max')

# Initialize the algorithm
dqn = DQN(scaler=scaler, action_scaler=action_scaler)

dataset = MDPDataset([], [], []) # Placeholder for dataset

# Placeholder for collecting dataset
n_episodes = 10
for _ in range(n_episodes):
    env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        next_state, reward, done, _ = env.step(action)
        dataset.append(env.state, action, reward, done)
        env.state = next_state

# Fit the algorithm with the dataset
dqn.fit(dataset, n_epochs=10)

# Evaluate the trained model
eval_episodes = 10
for _ in range(eval_episodes):
    env.reset()
    done = False
    while not done:
        action = dqn.predict(env.state)
        next_state, _, done, _ = env.step(action)
        env.state = next_state
    print(f'Episode {_+1} completed')