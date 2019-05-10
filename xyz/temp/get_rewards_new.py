# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 02:04:40 2019

@author: thnxe
"""

import pandas as pd
import numpy as np
df = pd.read_excel('trip.xlsx', sheet_name=0)
take_theta = df['Inclination'].tolist()
take_speed = df['Speed'].tolist()
take_reward= df['power_req'].tolist()
#theta=[]
a,b=0,0
c=-1.57
d=-1.67
rewards=[]
final_rewards=np.zeros([32,37])

def func(f,g):
    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for i,j,k in zip(take_theta,take_speed,take_reward):
     
        if(i<f and i >=g):
            if(j<1):
                s1.append(k)
            if(j>=1 and j<2):
                s2.append(k)
            if(j>=2 and j<3):
                s3.append(k)
            if(j>=3 and j<4):
                s4.append(k)
            if(j>=4 and j<5):
                s5.append(k)
            if(j>=5 and j<6):
                s6.append(k)
            if(j>=6 and j<7):
                s7.append(k)
            if(j>=7 and j<8):
                s8.append(k)
            if(j>=8 and j<9):
                s9.append(k)
            if(j>=9 and j<10):
                s10.append(k)
            if(j>=10 and j<11):
                s11.append(k)
            if(j>=11 and j<12):
                s12.append(k)
            if(j>=12 and j<13):
                s13.append(k)
            if(j>=13 and j<14):
                s14.append(k)
            if(j>=14 and j<15):
                s15.append(k)
            if(j>=15 and j<16):
                s16.append(k)
            if(j>=16 and j<17):
                s17.append(k)
            if(j>=17 and j<18):
                s18.append(k)
            if(j>=18 and j<19):
                s19.append(k)    
            if(j>=19 and j<20):
                s20.append(k)
            if(j>=20 and j<21):
                s21.append(k)
            if(j>=21 and j<22):
                s22.append(k)
            if(j>=22 and j<23):
                s23.append(k)
            if(j>=23 and j<24):
                s24.append(k)
            if(j>=24 and j<25):
                s25.append(k)
            if(j>=25 and j<26):
                s26.append(k)
            if(j>=26 and j<27):
                s27.append(k)
            if(j>=27 and j<28):
                s28.append(k)
            if(j>=28 and j<29):
                s29.append(k)
            if(j>=29 and j<30):
                s30.append(k)
            if(j>=30 and j<31):
                s31.append(k)
            if(j>=31 and j<32):
                s32.append(k)
            if(j>=32 and j<33):
                s33.append(k)
            if(j>=33 and j<34):
                s34.append(k)
            if(j>=34 and j<35):
                s35.append(k)
            if(j>=35 and j<36):
                s36.append(k)
            if(j>=36):
                s37.append(k)
    rewards.append(s1)
    rewards.append(s2)
    rewards.append(s3)
    rewards.append(s4)
    rewards.append(s5)
    rewards.append(s6)
    rewards.append(s7)
    rewards.append(s8)
    rewards.append(s9) 
    rewards.append(s10)
    rewards.append(s11)
    rewards.append(s12)
    rewards.append(s13)
    rewards.append(s14)
    rewards.append(s15)
    rewards.append(s16)
    rewards.append(s17)
    rewards.append(s18)
    rewards.append(s19)
    rewards.append(s20)
    rewards.append(s21)
    rewards.append(s22)
    rewards.append(s23)
    rewards.append(s24)
    rewards.append(s25)
    rewards.append(s26)
    rewards.append(s27)
    rewards.append(s28)
    rewards.append(s29) 
    rewards.append(s30)
    rewards.append(s31)
    rewards.append(s32)
    rewards.append(s33)
    rewards.append(s34)
    rewards.append(s35)
    rewards.append(s36)
    rewards.append(s37)
while(c<=1.63 and d<=1.53):
    func(c,d)
    c+=0.1
    d+=0.1
for c in range(31):
    for d in range(37):
        if not rewards[a]:          #there might be some combinations of states for which no actions are given 
            final_rewards[c][d]=0
            a=a+1
        else:
            final_rewards[c][d]=min(rewards[a])
            a=a+1

#print(final_rewards)


