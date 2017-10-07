# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:41:40 2017

@author: Yalda
This function counts the number of inversions in an array.
#number of pairs for which if i<j, A[i]>A[j] 
"""

def merge_countSplitInv(Left, Right):
    i, j = 0, 0
    Sorted_vec = []
    Invcount = 0
    
    for k in range(len(Left)+len(Right)):
        if Left[i] < Right[j]:
            
            Sorted_vec.append(Left[i])
            i = i+1

        else:

            Sorted_vec.append(Right[j])
            j = j+1
            Invcount = Invcount + (len(Left)-i)

        if i == len(Left):

            Sorted_vec.extend(Right[j:])
            break
        if j == len(Right):
            Sorted_vec.extend(Left[i:])
            break
    print('merging:', Sorted_vec)
    return Invcount, Sorted_vec

        

def sort_count(Input):
        
    
    print('splitting:', Input, len(Input))
    if len(Input)>1:
        
        
        count_L, LeftHalf = sort_count(Input[:(len(Input)//2)])
        print('left', LeftHalf)
        count_R, RightHalf= sort_count(Input[(len(Input)//2):])
        print('Right', RightHalf)
        count_all, merge_left_right = merge_countSplitInv(LeftHalf, RightHalf)

        return count_L+count_R+count_all, merge_left_right
    else:
        return 0, Input

           

Input = [1,3,7,5,2,4,6,0]
count_i, Input_s = sort_count(Input)
print('number of inversions:', count_i, ', sorted array:', Input_s)