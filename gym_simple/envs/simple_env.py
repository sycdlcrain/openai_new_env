import os, subprocess, time, signal
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
import numpy as np


import logging
logger = logging.getLogger(__name__)

class SimpleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.viewer = None
        self.server_process = None
        self.server_port = None
        
        self.max_pose = 5
        self.world = np.zeros(self.max_pose)
        self.player = 0

        self.observation_space = spaces.Box(low=0, high=1, shape=(np.shape(self.world)))
        self.action_space = spaces.Box(low=0, high=1, shape=1)


    def _step(self, action):
        if action==1:
            self.player+=1
        else:
            self.player-=1
        if self.player<0:
            self.player = 0

        observation = self.world + 0
        observation[self.player] = 1

        reward = self._get_reward()

        episode_over = False
        if self.player==self.max_pose-1:
            episode_over = True

        info = {}

        return observation, reward, episode_over, info

    def _get_reward(self):
        """ Reward is given for reaching the goal. """
        if self.player == self.max_pose-1:
            return 1
        else:
            return 0

    def _reset(self):
        """ Repeats NO-OP action until a new episode begins. """
        self.player = 0
        observation = self.world + 0
        observation[self.player] = 1
        return observation

    def _render(self, mode='human', close=False):
        """ Viewer only supports human mode currently. """
        print(self.player)

