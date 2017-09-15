import random

randomList = []
randomHundred = []

for i in range(0, 10000):
    randomNUmber = random.randint(0, 10000)
    randomList.append(randomNUmber)
# print(randomList)

for i in range(0, 100):
    randomNUmber = random.randint(0, 100)
    randomHundred.append(randomNUmber)
# print(randomHundred)

# for i in randomHundred:
#     if i in randomList:
#         print ('yes', i)
#     else:
#         print ('no', i)

def findNumber(num, listNum):
    for i in listNum:
        # print ('first', i)
        if (i == num):
            # print ('after check', i)
            return (True, num)
    # print ('if false', i)
    return (False, num)

# print(findNumber(3, [4,3,21,4422,431,34]))

for element in randomHundred:
    print(findNumber(element, randomList))