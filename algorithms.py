#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:56:21 2020

@author: albduranlopez
"""


#Complejidad O(n^2). Una kk
def burbujita(nums):
    seguir = True
    while seguir:
        seguir = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                seguir = True



#Complejidad O(n^2), también es malo
def selection(nums):
    for i in range(len(nums)):
        menor = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[menor]:
                menor = j
        nums[i], nums[menor] = nums[menor], nums[i]



#Luego vendrán mejor, o no...


#ej2
if __name__=="__main__":

    numeros = [6,8,4,3,2]
    
    burbujita(numeros)
    print(numeros)
    
    selection(numeros)
    print(numeros)
    