import random
from sa import *
class Environment:
    def __init__(self, state = 0, min_rpm =0, max_rpm = 5):
        self.state = state
        self.max_rpm = max_rpm
        self.min_rpm = min_rpm

    def take_action(self, action):
        if (action == Current_off):
            if (self.rpm == self.min_rpm):
                self.rpm = self.min_rpm
                reward = -5
            else:
                if self.rpm >0:
                    self.rpm-= 1
                if(self.rpm < 3):
                    reward = -1
                elif self.rpm==3:
                    reward =10
                else:
                    reward = 4
        if (action == Current_on):
            if (self.rpm == self.max_rpm):
                self.rpm = self.max_rpm
                reward = -5
            else:
                if self.rpm <5:
                    self.rpm+= 1
                if(self.rpm == 3):
                    reward = 10
                elif(self.rpm>3):
                    reward = -1
                else:
                    reward = 4
        return self.rpm, reward

    def reset(self):
        self.rpm = 0  # Reset state to zero, the beginning of dungeon
        return self.rpm
##o= Environment(0,0,100)

#o.take_action(random.choice((Current_on,Current_off)))