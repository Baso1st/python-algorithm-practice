
from os import stat
import random
from turtle import st

def quick_sort_old(list:list, startIndex = 0, endIndex = 0):
    if endIndex <= startIndex:
        return
    
    arrayLength = (endIndex - startIndex) + 1
    piviotIndex = startIndex + random.randint(0, arrayLength )
    piviot = list[piviotIndex]
    leftList = [-1] * arrayLength
    rightList = [-1] * arrayLength
    j = k = 0
    for i in range(startIndex, endIndex + 1):
        if i == piviotIndex:
            continue
        if list[i] <= piviot:
            leftList[j] = list[i]
            j += 1
        else:
            rightList[k] = list[i]
            k += 1
    
    for i in range(j):
        list[startIndex + i] = leftList[i]
    
    list[startIndex + j] = piviot
    
    for i in range(k):
        list[startIndex + j + 1 + i] = rightList[i]

    quick_sort(list, startIndex, (startIndex + j)-1)
    quick_sort(list, startIndex + j + 1, endIndex)

     
    
def quick_sort(list: list, start, end):
    if start >= end:
        return
    
    p = partition(list, start, end)

    quick_sort(list, start, p-1)
    quick_sort(list, p + 1, end)


def partition(list: list, start, end):

    piviotIndex = start
    # piviotIndex = start + ( ((end - start) + 1) // 2)
    piviot = list[piviotIndex]

    while start < end:
        
        while start < len(list) and list[start] <= piviot:
            start += 1

        
        while list[end] > piviot:
            end -= 1

        
        if start < end:
            list[start], list[end] = list[end], list[start]
        
    list[end], list[piviotIndex] = list[piviotIndex], list[end]
    
    return end
