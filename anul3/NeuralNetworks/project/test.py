import numpy as np
import gym

env = gym.make('BipedalWalker-v3', render_mode="human")
print(env.action_space, env.observation_space.shape[0])
# print(env.reset())
env = gym.make('CarRacing-v2', render_mode="human", continuous=True)
print(env.action_space, int(np.prod(env.observation_space.shape)))
actions = env.action_space.shape
print(env.action_space.shape[0])
print(int(np.prod(env.action_space.shape)))
print(int(np.prod(env.observation_space.shape)))