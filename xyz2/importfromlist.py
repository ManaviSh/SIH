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
    if(i<-1.57):
        theta.append(0)
    if(i<-1.47 and i>=-1.57):    
        theta.append(1)
    if(i<-1.37 and i>=-1.47):    
        theta.append(2)
    if(i<-1.27 and i>=-1.37):    
        theta.append(3)
    if(i<-1.17 and i>=-1.27):    
        theta.append(4)
    if(i<-1.07 and i>=-1.17):    
        theta.append(5)
    if(i<-0.97 and i>=-1.07):    
        theta.append(6)
    if(i<-0.87 and i>=-0.97):    
        theta.append(7)
    if(i<-0.77 and i>=-0.87):    
        theta.append(8)
    if(i<-0.67 and i>=-0.77):    
        theta.append(9)
    if(i<-0.57 and i>=-0.67):    
        theta.append(10)
    if(i<-0.47 and i>=-0.57):    
        theta.append(11)
    if(i<-0.37 and i>=-0.47):    
        theta.append(12)
    if(i<-0.27 and i>=-0.37):    
        theta.append(13)
    if(i<-0.17 and i>=-0.27):    
        theta.append(14)
    if(i<-0.07 and i>=-0.17):    
        theta.append(15)
    if(i<0.03 and i>=-0.07):    
        theta.append(16)
    if(i<0.13 and i>=0.03):    
        theta.append(17)
    if(i<0.23 and i>=0.13):    
        theta.append(18)
    if(i<0.33 and i>=0.23):    
        theta.append(19)
    if(i<0.43 and i>=0.33):    
        theta.append(20)
    if(i<0.53 and i>=0.43):    
        theta.append(21)
    if(i<0.63 and i>=0.53):    
        theta.append(22)
    if(i<0.73 and i>=0.63):    
        theta.append(23)
    if(i<0.83 and i>=0.73):    
        theta.append(24)
    if(i<0.93 and i>=0.83):    
        theta.append(25)
    if(i<1.03 and i>=0.93):    
        theta.append(26)
    if(i<1.13 and i>=1.03):    
        theta.append(27)
    if(i<1.23 and i>=1.13):    
        theta.append(28)
    if(i<1.33 and i>=1.23):    
        theta.append(29)
    if(i<1.43 and i>=1.33):    
        theta.append(30)
    if( i>=1.43):    
        theta.append(31)
#    if(i<1.67 and i>=1.57):    
#        theta.append(1)
#    if(i<1.77 and i>=1.67):    
#        theta.append(1)
#    if(i<1.87 and i>=1.77):    
#        theta.append(1)
#    if(i<1.97 and i>=1.87):    
#        theta.append(1)
#    
print(max(theta))
curr_state=list(zip(time,theta))
next_states=list(zip(time,theta[1:]))
#print(next_state)
#pro_trans=pd.crosstab(pd.Series(t[1:],name='Tomorrow'),
#            pd.Series(t[:-1],name='Today'),normalize=1)
#print(pro_trans)
        