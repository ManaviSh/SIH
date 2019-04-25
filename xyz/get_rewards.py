# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:58:05 2019

@author: thnxe
"""

import pandas as pd
import numpy as np
df = pd.read_excel('Trip_1.xls', sheet_name=0)
take_theta = df['Inclination'].tolist()
take_speed = df['Speed'].tolist()
take_power = df['power_req'].tolist()
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s6=[]
s7=[]
s8=[]
s9=[]
s10=[]
s11=[]
s12=[]
s13=[]
s14=[]
s15=[]
s16=[]
#theta=[]
a,b=0,0
rewards=[]
final_rewards=np.zeros([4,4])

for i,j,k in zip(take_theta,take_speed,take_power):
    if(i<0.5):
        if(j<4):
            s1.append(k)   
        if(j>=4 and j<8):
            s2.append(k)
        if(j>=8 and j<12):
            s3.append(k)
        if(j>=12):
            s4.append(k)
   # rewards=[s1,s2,s3,s4]

#print(len(rewards))
#print(len(rewards[0]))

            
    if(i>=0 and i<0.5):
        if(j<4):
            s5.append(k)
        if(j>=4 and j<8):
            s6.append(k)
        if(j>=8 and j<12):
            s7.append(k)
        if(j>=12):
            s8.append(k)
    
    
    if(i>=0.5 and i<1):
        if(j<4):
            s9.append(k)
        if(j>=4 and j<8):
            s10.append(k)
        if(j>=8 and j<12):
            s11.append(k)
        if(j>=12):
            s12.append(k)
    
    if(i>=1):
        if(j<4):
            s13.append(k)
        if(j>=4 and j<8):
            s14.append(k)
        if(j>=8 and j<12):
            s15.append(k)
        if(j>=12):
            s16.append(k)
rewards=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16]
#if(rewards[0]==s1):
#    print('true')
#else:
#    print('false')

for c in range(4):
    for d in range(4):
        final_rewards[c][d]=max(rewards[a])
        a=a+1
#print(final_rewards)
            
            
            
            
            
            
#        s1.append(i)
#        theta.append(1)
#    if(i>=-0.5 and i<0):
#        s2.append(i)
#        theta.append(2)
#    if(i>=0 and i<0.5):
#        s3.append(i)
#        theta.append(3)
#    if(i>=0.5):
#        s4.append(i)
#        theta.append(4)
