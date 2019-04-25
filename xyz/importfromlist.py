# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:38:42 2019

@author: thnxe
"""



import pandas as pd
#t = [1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
df = pd.read_excel('Trip_1.xls', sheet_name=0) 
mylist = df['Inclination'].tolist()
time = df['Time'].tolist()
#s1=[]
#s2=[]
#s3=[]
#s4=[]
theta=[]
for i in mylist:
    if(i<0):
        #s1.append(i)
        theta.append(0)
    if(i>=0 and i<0.5):
        #s2.append(i)
        theta.append(1)
    if(i>=0.5 and i<1):
        #s3.append(i)
        theta.append(2)
    if(i>=1):
        #s4.append(i)
        theta.append(3)
#print(theta)
curr_state=list(zip(time,theta))
next_states=list(zip(time,theta[1:]))
#print(next_state)
#pro_trans=pd.crosstab(pd.Series(t[1:],name='Tomorrow'),
#            pd.Series(t[:-1],name='Today'),normalize=1)
#print(pro_trans)
        
