# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 02:04:40 2019

@author: thnxe
"""

import pandas as pd
import numpy as np
df = pd.read_excel('Trip_1.xls', sheet_name=0)
take_theta = df['Inclination'].tolist()
take_speed = df['Speed'].tolist()
take_power = df['power_req'].tolist()
s1=np.array
#theta=[]
a,b=0,0
rewards=[]
final_rewards=np.zeros([32,18])
def func(f,g):
    s1=[]
    s2=[]
    s3=[]
    s4=[]
    s5=[]
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
    s17=[]
    s18=[]
    for i,j,k in zip(take_theta,take_speed,take_power):
        if(i<f and i >=g):
            if(j<1):
                s1.append(k)
#            s.append(s1)
            if(j>=1 and j<2):
                s2.append(k)
                #            s.append(s2)
                if(j>=2 and j<3):
                    s3.append(k)
#            s.append(s3)
            if(j>=3 and j<4):
                s4.append(k)
#            s.append(s4)
            if(j>=4 and j<5):
                s5.append(k)
#            s.append(s5)
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
            if(j>=17):
                s18.append(k)
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
func(-1.57,-10)
func(-1.47,-1.57)
func(-1.37,-1.47)
func(-1.27,-1.37)
func(-1.17,-1.27)
func(-1.07,-1.17)
func(-0.97,-1.07)
func(-0.87,-0.97)
func(-0.77,-0.87)
func(-0.67,-0.77)
func(-0.57,-0.67)
func(-0.47,-0.57)
func(-0.37,-0.47)
func(-0.27,-0.37)
func(-0.17,-0.27)
func(-0.07,-0.17)
func(0.03,-0.07)
func(0.13,0.03)
func(0.23,0.13)
func(0.33,0.23)
func(0.43,0.33)
func(0.53,0.43)
func(0.63,0.53)
func(0.73,0.63)
func(0.83,0.73)
func(0.93,0.83)
func(1.03,0.93)
func(1.13,1.03)
func(1.23,1.13)
func(1.33,1.23)
func(1.43,1.33)
func(2,1.43)
for c in range(31):
    for d in range(18):
        if not rewards[a]:
            final_rewards[c][d]=0
            a=a+1
        else:
            final_rewards[c][d]=max(rewards[a])
            a=a+1




