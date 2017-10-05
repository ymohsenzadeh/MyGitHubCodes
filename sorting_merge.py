# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:50:15 2017

@author: Yalda Mohsenzadeh
# Sortting a list with sort merge algorithm
"""
def merge(Left, Right):
    i, j = 0, 0
    Sorted_vec = []
    
    for k in range(len(Left)+len(Right)):
        if Left[i] > Right[j]:
            
            Sorted_vec.append(Left[i])
            i = i+1

        else:

            Sorted_vec.append(Right[j])
            j = j+1 

        if i == len(Left):

            Sorted_vec.extend(Right[j:])
            break
        if j == len(Right):
            Sorted_vec.extend(Left[i:])
            break
    print('merging:', Sorted_vec)
    return Sorted_vec

        

def mergesort(Input):
        
    
    print('splitting:', Input, len(Input))
    if len(Input)>1:
        
        
        LeftHalf = mergesort(Input[:(len(Input)//2)])
        print('left', LeftHalf)
        RightHalf= mergesort(Input[(len(Input)//2):])
        print('Right', RightHalf)

        return merge(LeftHalf, RightHalf)
    else:
        return Input

           

Input = [3,4,5,1,2,8,3,7,6,0, 11,0,7]
Input_s = mergesort(Input)
print('sorted', Input_s)