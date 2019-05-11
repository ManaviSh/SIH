import random
from actions import *
from states import *
from rewards import reward
rew=reward()
class Environment:
    def __init__(self, state_length, min_state, max_state, action_length):
        self.state_length = 63
        self.min_state = -1.57
        self.max_state = 1.57
        self.action_length = 116

    def take_action(self, curr_action, state):
        reward = rew.get_reward(curr_action, state)
        return state+1, reward

    def reset(self):
        self.state = 0 #
        return self.state