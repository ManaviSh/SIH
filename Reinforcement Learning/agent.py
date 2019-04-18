from sa import *
import random
import numpy as np

class car:
    def __init__(self, learning_rate=0.001, discount=0.98, exploration_rate=1.0, iterations=10000):
        self.q_table = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] # Spreadsheet (Q-table) for rewards accounting
        self.learning_rate = learning_rate # How much we appreciate new q-value over current
        self.discount = discount # How much we appreciate future reward over current
        self.exploration_rate = 1.0 # Initial exploration rate
        self.exploration_delta = 0.001# Shift from exploration to explotation

    def get_next_action(self, rpm):
        if random.random() > self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.greedy_action(rpm)
        else:
            return self.random_action()

    def greedy_action(self, rpm):
        # Is FORWARD reward is bigger?
        if self.q_table[Current_on][rpm] > self.q_table[Current_off][rpm]:
            return Current_on
        # Is BACKWARD reward is bigger?
        elif self.q_table[Current_off][rpm] > self.q_table[Current_on][rpm]:
            return Current_off
        # Rewards are equal, take random action
        return Current_on if random.random() < 0.5 else Current_off

    def random_action(self):
        return Current_on if random.random() < 0.5 else Current_on

    def update(self, old_rpm, new_rpm, action, reward):
        # Old Q-table value
        old_value = self.q_table[action][old_rpm]
        # What would be our best next action?
        future_action = self.greedy_action(new_rpm)
        # What is reward for the best next action?
        future_reward = self.q_table[future_action][new_rpm]

        # Main Q-table updating algorithm
        new_value = old_value + self.learning_rate * (reward + self.discount * future_reward - old_value)
        self.q_table[action][old_rpm] = new_value

        # Finally shift our exploration_rate toward zero (less gambling)
        if self.exploration_rate > 0:
            self.exploration_rate -= self.exploration_delta