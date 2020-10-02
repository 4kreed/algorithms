#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:56:21 2020

@author: albduranlopez
"""


#Complejidad O(n^2). Una kk
def Burbujita(nums):
    seguir = True
    while seguir:
        seguir = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                seguir = True



if __name__=="__main__":

    numeros = [6,8,4,3,2]
    Burbujita(numeros)
    print(numeros)
    
    numeros2 = [3,33,333,5.4]
    Burbujita(numeros2)
    print(numeros2)
    