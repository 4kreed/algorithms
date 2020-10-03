#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: albduranlopez
"""


#Complejidad O(n^2). Una kk, mal
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


#Complejidad O(n^2), joe
def insertion(nums):
    for i in range(1, len(nums)):
        insertar = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > insertar:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = insertar
        
        
        
#ej2
if __name__=="__main__":

    numeros = [6,8,4,3,2]
    
    burbujita(numeros)
    print(numeros)
    
    selection(numeros)
    print(numeros)
    
    
    numeros = [6,8,4,56,2]
    insertion(numeros2)
    print(numeros2)
    
    
    
    
    
    
    