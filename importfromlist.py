# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:38:42 2019

@author: thnxe
"""

#import xlwings as xw
#
#wb = xw.Book('Trip_1.xls')
#sht = xw.Book('Scan Tool Data')
#py_list = sht.range('L2:L586').value


import pandas as pd

df = pd.read_excel('Trip_1.xls', sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = df['Inclination'].tolist()
theta1=[]
#theta2=[]
#theta3=[]
#theta4=[]
#theta1.append(0)
#print(theta1)
for i in mylist:
    if(i<-0.5):
        theta1.append('state1')
    if(i>=-0.5 and i<0):
        theta1.append('state2')
    if(i>=0 and i<0.5):
        theta1.append('state3')
    if(i>=0.5):
        theta1.append('state4')
print(pd.crosstab(pd.Series(theta1[1:],name='Tomorrow'),
            pd.Series(theta1[:-1],name='Today'),normalize=1).values)

        