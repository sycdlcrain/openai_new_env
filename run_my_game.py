import gym

import gym_simple
import numpy as np

game_name = 'simple-v0'
print("Starting", game_name)

env = gym.make(game_name)
print("observation space", env.observation_space)
print("action space", env.action_space) 

frameskip = 1
### SETUP SECARIO ###
for i in range(1000):

	env.reset()
	done = False
	cumulative_reward = 0
	# for j in xrange(100):
	while not done:

		action = np.random.randint(0,2)
		
		for f in range(frameskip):
			observation, reward, done, info = env.step(action)
			cumulative_reward += reward

		env.render()
		
		if done==True:
			print("yay!!")
			break
	print(cumulative_reward)
