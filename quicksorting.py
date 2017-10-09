# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:24:01 2017

@author: Yalda Mohsenzadeh
"""
#This is an implementation of quicksort algorithm in python

from random import randrange

def partition(A, l, r):
    
    pivot = A[l]
    i = l+1
    
    for j in range(l+1,r+1):
        if A[j]<pivot: # if A[j]<=pivot do nothing
            # swap A[j] and pivot
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i = i+1
    
    # swap A[l] and A[i-1] to put pivot in its real position        
    temp = A[i-1]
    A[i-1] = A[l]
    A[l] = temp
    
    return A, i-1
    
def quicksort(A, lenA):
    if lenA <=1:
        return A
    else:  
        Pivot_index = randrange(0, lenA) # random selection of pivot
        #move selected pivot to the first position in the array
        temp =A[0]
        A[0] = A[Pivot_index]
        A[Pivot_index] = temp
        
        # partition the array around pivot
        A, pivot_real_position = partition(A, 0, lenA-1)
       
        A[:pivot_real_position] = quicksort(A[:pivot_real_position], len(A[:pivot_real_position]))
        A[pivot_real_position+1:] = quicksort(A[pivot_real_position+1:], len(A[pivot_real_position+1:]))
        return A


#A = ['yalda', 'alex', 'ali', 'hossein', 'mohsenzadeh']
A = [ 3, 8, 2, 5, 1, 4, 7, 6, 6]
sortedA = quicksort(A, len(A))
print('sorted:', sortedA)