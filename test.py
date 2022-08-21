from rlgridworld.gridenv import GridEnv
import numpy as np


env = GridEnv(load_chars_rep_fromd_dir = 'EnvSettings/SimpleTarget.txt')
env.reset()
print(env.init_chars_representation)
env.step(action = env.actions.UP())
print(env.chars_world)