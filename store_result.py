## problem to find, the elements of first array in second array
# store those elements in another array list 
# if we have repeated elements in array, find the repeated elements in newly created list

import random

randomList = ['2','34','21','16','64','76','98','89','123','768','2113','96','23','52','99']
randomHundred = ['89','96','123','23','100','23']
resultStore = []

def findNumber(num, listNum):
    for i in listNum:
        if (i == num):
            resultStore.append(num)
            return (True, resultStore)
    return (False, num)

for element in randomHundred:
    if element in resultStore:
        print ('from existing result', element)
        print(findNumber(element, resultStore))
    elif element in randomList:
        print ('from main', element)
        print(findNumber(element, randomList))
