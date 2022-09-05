# binary search
# Adam Prado
# 9/5/22

import random
import math

def randomListNumbers(maxV,listLen):
    Nlist = []
    for i in range(listLen):
        Nlist.append(random.randint(0, maxV))
    return Nlist

def binSearch(listIn,value):
    firstInd = 0
    lastInd = len(listIn)
    midInd = math.floor((firstInd + lastInd)/2)
   
    while listIn[midInd] != value:
        if listIn[midInd]<value:
            firstInd = midInd
        else:
            lastInd = midInd
        midInd = math.floor((firstInd + lastInd)/2)
        if firstInd==midInd or lastInd==midInd:
            return -1
    return midInd

randListTest = randomListNumbers(10,20)
print("random list of numbers")
print(randListTest)
randListTest.sort()
print("sorted list")
print(randListTest)
print("test to find index with value of 2")
print(binSearch(randListTest,2))
print("test to find index with value of 8")
print(binSearch(randListTest,8))
print("test to find index with value of 11, should not be in list and return -1")
print(binSearch(randListTest,11))