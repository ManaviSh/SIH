from actions import *
import random
import numpy as np

class car:
    def __init__(self, learning_rate=0.001, discount=0.98, exploration_rate=1.0, iterations=10000):
        self.q_table = np.zeros((63, 116)) # Spreadsheet (Q-table) for rewards accounting
        self.learning_rate = learning_rate # How much we appreciate new q-value over current
        self.discount = discount # How much we appreciate future reward over current
        self.exploration_rate = 1.0 # Initial exploration rate
        self.exploration_delta = 0.001# Shift from exploration to explotation

    def get_next_action(self, state):
        if random.uniform(0, 1) > 0.5: # 
            return self.greedy_action(state)
        else:
            return self.random_action()

    def greedy_action(self, state):
            return np.argmax(self.q_table[state])

    def random_action(self):
        return random.choice(actions)

    def update(self, old_state, new_state, curr_action, reward):
        # Old Q-table value
        action=np.where(actions==curr_action)
        old_value = self.q_table[old_state][action] #pta chla?float aa rhi h teri action ki value apne action waale numpy array ko .astype(int) laga
        # What would be our best next action?
        future_action = self.get_next_action(new_state)
        # What is reward for the best next action?
        future_reward = self.q_table[new_state][future_action]

        # Main Q-table updating algorithm
        new_value = old_value + self.learning_rate * (reward + self.discount * future_reward - old_value)
        self.q_table[old_state][action] = new_value

        # Finally shift our exploration_rate toward zero (less gambling)
        if self.exploration_rate > 0:
            self.exploration_rate = self.exploration_delta - 0.2
