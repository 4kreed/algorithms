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
        
        
        
        

def merge(izq, dcha):
    if len(izq) == 0:
        return dcha

    if len(dcha) == 0:
        return izq

    dev = []
    index_izq = index_dcha = 0

   
    while len(dev) < len(izq) + len(dcha):
       
        if izq[index_izq] <= dcha[index_dcha]:
            dev.append(izq[index_izq])
            index_izq += 1
        else:
            dev.append(dcha[index_dcha])
            index_dcha += 1

       
        if index_dcha == len(dcha):
            dev += izq[index_izq:]
            break

        if index_izq == len(izq):
            dev += dcha[index_dcha:]
            break

    return dev


def mergesort(nums):
    if len(nums) < 2:
        return nums

    mitad = len(nums) // 2
    return merge(mergesort(nums[:mitad]),mergesort(nums[mitad:]))


#valid
class parenthesis:
   def check_if_correct_parent(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(parenthesis().check_if_correct_parent("(){}[]"))
print(parenthesis().check_if_correct_parent("()[{)}"))
print(parenthesis().check_if_correct_parent("()"))



#ej2
if __name__=="__main__":

    numeros = [6,8,4,3,2]
    
    burbujita(numeros)
    print(numeros)
    
    selection(numeros)
    print(numeros)
    
    insertion(numeros)
    print(numeros)
    
    mergesort(numeros)
    print(numeros)
    
    
    
    
    
    
    
