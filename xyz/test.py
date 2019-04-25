# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 00:02:56 2019

@author: thnxe
"""
import numpy as np
import random
from importfromlist import next_states
from get_rewards import final_rewards
from IPython.display import clear_output
alpha = 0.1
gamma = 0.6
epsilon = 0.1
actions=[0,1,2,3]
states=[0,1,2,3]
ns=4
max_epochs=1312
q_table = np.zeros([4, 4])
#actions=np.asarray(actions)
#def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
#final_rewards=[[1,-10,0,1],
#               [1,-10,0,1],
#               [1,-10,0,1],
#               [1,-10,0,1]]     
for i in range(0,max_epochs):
        state = np.random.randint(0,ns)
        done = False
        epochs, penalties, reward, = 0, 0, 0
    
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions) # Explore action space
            else:
                action = np.argmax(q_table[state]) # Exploit learned values
    
            for a in next_states:
                if(a[0]==i):
                    next_state=a[1]
            reward=final_rewards[state][action]
        
            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value
            
            if reward == -10:
                penalties += 1
                
            state = next_state
            epochs += 1
            
        if i % 100 == 0:
            clear_output(wait=True)
            print(f"Episode: {i}")
            
            
print("Training finished.\n")
        
