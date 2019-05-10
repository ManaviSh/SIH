# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:00:51 2019

@author: thnxe
"""
#from test1 import policy
#import numpy as np
#p=[]
#for i in range(len(policy)):
#    if(policy[i]>0):
#        p.append(i)
#        
#print(p)
from test1 import policy
import numpy as np
import pandas as pd
from ev import vehicle
import matplotlib.pyplot as plt 
import numpy as np

data = pd.read_excel ('Trip_1.xls') 
df = pd.DataFrame(data, columns= ['Time','Speed', 'Acceleration', 'Inclination_x', 'Inclination_y', 'Power(kW)', 'Inclination'])
d = np.array(df.as_matrix())
Time = d[:, 0]
Speed = d[:, 1]
Acceleration = d[:, 2]
Inclination_x = d[:, 3] #cos theta
Inclination_y = d[:, 4] #sin theta
Pw = d[:, 5]
inclination=d[:,6]
m=0
c=-1.57
d=-1.67
s1=[]

#def func(f,g):
for i in inclination:
  
    if(i<-1.57):
        m=0;
    if(i<-1.47 and i>=-1.57):    
        m=1;
    if(i<-1.37 and i>=-1.47):    
        m=2;
    if(i<-1.27 and i>=-1.37):    
        m=3;
    if(i<-1.17 and i>=-1.27):    
        m=4;
    if(i<-1.07 and i>=-1.17):    
        m=5;
    if(i<-0.97 and i>=-1.07):    
        m=6;
    if(i<-0.87 and i>=-0.97):    
        m=7;
    if(i<-0.77 and i>=-0.87):    
        m=8;
    if(i<-0.67 and i>=-0.77):    
        m=9;
    if(i<-0.57 and i>=-0.67):    
        m=10;
    if(i<-0.47 and i>=-0.57):    
        m=11;
    if(i<-0.37 and i>=-0.47):    
        m=12;
    if(i<-0.27 and i>=-0.37):    
        m=13;
    if(i<-0.17 and i>=-0.27):    
        m=14;
    if(i<-0.07 and i>=-0.17):    
        m=15;
    if(i<0.03 and i>=-0.07):    
        m=16;
    if(i<0.13 and i>=0.03):    
        m=17;
    if(i<0.23 and i>=0.13):    
        m=18;
    if(i<0.33 and i>=0.23):    
        m=19;
    if(i<0.43 and i>=0.33):    
        m=20;
    if(i<0.53 and i>=0.43):    
        m=21;
    if(i<0.63 and i>=0.53):    
        m=22;
    if(i<0.73 and i>=0.63):    
        m=23;
    if(i<0.83 and i>=0.73):    
        m=24;
    if(i<0.93 and i>=0.83):    
        m=25;
    if(i<1.03 and i>=0.93):    
        m=26;
    if(i<1.13 and i>=1.03):    
        m=27;
    if(i<1.23 and i>=1.13):    
        m=28;
    if(i<1.33 and i>=1.23):    
        m=29;
    if(i<1.43 and i>=1.33):    
        m=30;
    if( i>=1.43):    
        m=31;
#    if(i<f and i >=g):

    j=policy[m]
    if(j==0):
        s1.append(1)
    if(j==1):
        s1.append(2)
    if(j==2):
        s1.append(3)
    if(j==3):
        s1.append(4)
    if(j==4):
        s1.append(5)
    if(j==5):
        s1.append(6)
    if(j==6):
        s1.append(7)
    if(j==7):
        s1.append(8)
    if(j==8):
        s1.append(9)
    if(j==9):
        s1.append(10)
    if(j==10):
        s1.append(11)
    if(j==11):
        s1.append(12)
    if(j==12):
        s1.append(13)
    if(j==13):
        s1.append(14)
    if(j==14):
        s1.append(15)
    if(j==15):
        s1.append(16)
    if(j==16):
        s1.append(17)    
    if(j==17):
        s1.append(18)
    if(j==18):
        s1.append(19)
    if(j==19):
        s1.append(20)
    if(j==20):
        s1.append(21)
    if(j==21):
        s1.append(22)
    if(j==22):
        s1.append(23)
    if(j==23):
        s1.append(24)
    if(j==24):
        s1.append(25)
    if(j==25):
        s1.append(26)
    if(j==26):
        s1.append(27)
    if(j==27):
        s1.append(28)
    if(j==28):
        s1.append(29)
    if(j==29):
        s1.append(30)
    if(j==30):
        s1.append(31)
    if(j==31):
        s1.append(32)
    if(j==32):
        s1.append(33)
    if(j==33):
        s1.append(34)
    if(j==34):
        s1.append(35)
    if(j==35):
        s1.append(36)
    if(j==36):
        s1.append(37)
#            if(j==37):
#                s1.append(1)            
#while(c<=1.63 and d<=1.53):
#    func(c,d)
#    c+=0.1
#    d+=0.1

speed1= np.array(s1)
def main():
    Power = vehicle()
    P = Power.Power_Required(Speed, Inclination_x, Inclination_y, Acceleration)
    #from test1 import acc,vel
    Pw = Power.Power_Required(speed1, Inclination_x, Inclination_y, Acceleration)
    plt.plot(Time, Pw, label = "Obs")  
    plt.plot(Time, P, label = "Power Required") 
    plt.xlabel('Time')
    plt.ylabel('y - axis')
    plt.title('Comparision') 
    plt.legend() 
    plt.show() 
    with open('do_2.csv', 'wb') as abc:
       np.savetxt(abc, P, delimiter=",")
    
if __name__ == "__main__":
    main()