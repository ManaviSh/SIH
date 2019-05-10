# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:56:33 2019

@author: thnxe
"""

import numpy as np
import time
import os
import random
from importfromlist import next_states
from get_rewards_new import final_rewards
from IPython.display import clear_output
alpha = 0.1
gamma = 0.6 
epsilon = 0.1
#actions=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#states=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
states=np.arange(32)
actions=np.arange(37)
ns=32
na=37
max_epochs=132124
q_table = np.zeros([32, 37])
policy=np.zeros(32)

# create environment
#env = Env()

# QTable : contains the Q-Values for every (state,action) pair
qtable = np.random.rand(32,37).tolist()

# hyperparameters
epochs = 50
gamma = 0.1
epsilon = 0.08
decay = 0.1

# training loop
for i in range(max_epochs):
#    state, reward,done = env.reset()
    steps = 0

#    while not done:
#        os.system('clear')
#        print("epoch #", i+1, "/", epochs)
#        env.render()
#        time.sleep(0.05)

        # count steps to finish game
        #steps += 1
    #while(True):
    state = np.random.randint(0,ns)
        
        # act randomly sometimes to allow exploration
    if np.random.uniform() < epsilon:
        action = np.random.choice(actions)
        # if not select max action in Qtable (act greedy)
    else:
        action = qtable[state].index(max(qtable[state]))
            
            
    reward=final_rewards[state][action]
        # take action
        #next_state, reward, done = env.step(action)
    for a in next_states:
        if(a[0]==i):            #
            next_state=a[1]

        # update qtable value with Bellman equation
    qtable[state][action] = reward + gamma * max(qtable[next_state])

        # update state
    state = next_state
    # The more we learn, the less we take random actions
    epsilon -= decay*epsilon
    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")
            
            


    #print("\nDone in", steps, "steps".format(steps))
    #time.sleep(0.8)
print("Training finished.\n")
#print(q_table)
for i in range(ns):
    policy[i]=np.argmax(qtable[i])
print(policy)