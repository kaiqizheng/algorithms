# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:41:49 2018

@author: user
"""

# return the ascending sorint list
def bigSorting(arr): # input arr is a list of str(numbers)
    arr.sort(key=int)        
    return arr

# return the index loaction of V in list "arr"
def introTutorial(V, arr):
    return arr.index(V)

# Given a sorted list with an unsorted number in the rightmost cell (2 4 6 8 5)
def insertionSort1(n, arr):
    temp=0
    j=0
    for i in range(1,n):
        temp=arr[i]
        j=i
        while(j>0 and arr[j-1]>temp):
        # j>0&j=j-1: backwards
        # arr[j-1]>temp: the starting point
            arr[j]=arr[j-1] # shift right
            j=j-1 # backwards
            print(' '.join([str(x) for x in arr])) # print every shifts
        arr[j]=temp # if while: j = 0 or arr[j-1]<=temp; if not while: nothing happened.
    print(' '.join([str(x) for x in arr]))

# sort an entire array based on method above (insertionSort1)
def insertionSort2(n, arr):
    temp=0
    j=0
    for m in range(2,n+1):
        for i in range(1,m):
            temp=arr[i]
            j=i
            while(j>0 and arr[j-1]>temp):
                arr[j]=arr[j-1]
                j=j-1
            arr[j]=temp
        print(' '.join([str(x) for x in arr]))

