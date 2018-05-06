# -*- coding: utf-8 -*-
"""
Created on Wed May  2 01:02:53 2018

@author: Kaiqi Zheng
"""

def findNumber(arr,k):
    if (k in arr):
        print("YES")
    else:
        print("NO")

# find the odd numbers between l and r        
def findOdd(l,r):
    if (l%2==1 and r%2==1):
        arr=[i for i in range(l,r+1,2)]
    elif (l%2==1 and r%2==0):
        arr=[i for i in range(l,r,2)]
    elif (l%2==0 and r%2==1):
        arr=[i for i in range(l+1,r+1,2)]
    elif (l%2==0 and r%2==0):
        arr=[i for i in range(l+1,r,2)]
    return arr
