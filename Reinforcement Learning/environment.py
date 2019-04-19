'''
    Random testing of making the agent learn a best rpm based on hard coded rewards. Even  with this essentially the problem was that even
    after destined iterations and satisfactory performance, the updated Q-table ony had all 0 as state action values for when the action is 
    current off
'''

import random
from sa import * #import action
class Environment:
    def __init__(self, rpm = 0, min_rpm = 0, max_rpm = 4):
        self.rpm = rpm
        self.min_rpm = min_rpm
        self.max_rpm = max_rpm

    def take_action(self, action):
        if (action == Current_off):
            if (self.rpm == self.min_rpm):
                self.rpm = self.min_rpm
                reward = -5
            else:
                if self.rpm >0:
                    self.rpm-= 1
                if(self.rpm < 3):
                    reward = 0
                elif self.rpm==3:
                    reward =10
                else:
                    reward = 7
        if (action == Current_on):
            if (self.rpm == self.max_rpm):
                self.rpm = self.max_rpm
                reward = -4
            else:
                if self.rpm <5:
                    self.rpm+= 1
                if(self.rpm == 3):
                    reward = 10
                else:
                    if(self.rpm<3):
                        reward = 5
                    else:
                        reward = 0
        return self.rpm, reward

    def reset(self):
        self.rpm = 0  # Reset state to zero, the beginning of trip
        return self.rpm
##o= Environment(0,0,100)

#o.take_action(random.choice((Current_on,Current_off)))
