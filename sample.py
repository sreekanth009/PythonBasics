# # Variables #

# a = 10
# b = 'hello..'
# c = 10.323
# print (a, b)

# # Variable Check #

# type_1 = type(a)
# type_2 = type(b)
# print(type_1, type_2)

# # Adding two Variable #

# num_1 = 10
# num_2 = 20
# num_sum = num_1 + num_2
# print(num_sum)

# # Adding two strings #

# str_1 = 'hello'
# str_2 = 'world'
# str_sum = str_1 + str_2
# print(str_sum)

# # check which is greater #

# if num_2 > num_1:
#     print str(num_2) + 'is greater'
# else:
#     print str(num_1) + 'is greater'

# # Basic for loop #

# for i in range(0, 10):
#     print(i)

# # even number from 0-100 #

# for x in range(0,100):
#     if x % 2 == 0:
#         print x

# multiples of 3,5 and both from 0-100 #

# for y in range(0, 100):
#     if (y % 3 == 0 and y % 5 ==0):
#         print(y, 'FizzBuzzz')
#     elif y % 3 == 0:
#         print(y, 'Fizz')
#     elif y % 5 == 0:
#         print(y, 'Buzzz')
#     else:
#         print(y)

# for x in range(0, 100):
#     if x % 5 == 0:
#         if x % 3 == 0:
#             print(x, 'FizzBuzz');
#         else:
#             print(x, 'Buzz');
#     elif x % 5 == 0:
#         print(x, 'Buzz');
#     elif x % 3 == 0:
#         print(x, 'Fizz');
#     else:
#         print(x);

## inverting the vowels in a string to upper to lower or viceversa #

# how do i check if its lowercase or Uppercase
# how do i check for vowels in the string
# if lowercase then make it uppercase
# if uppsercase then make it lowecase
# Print the string with inverted format

## Method 1 with pushing to new variable by inverting the vowels to upper or lower 

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# sentence = raw_input()
# finalString = ""
# for char in sentence:
#     print('for', char)
#     if char in vowels and char.isupper():
#         print('if', char)
#         finalString += char.lower()
#         # newSentence = sentence.swapcase()
#         # newSentence = sentence.replace(char, (char.lower()))
#         print('after if', finalString)
#     elif char in vowels and char.islower():
#         print('elif', char)
#         finalString += char.upper()
#         # newSentence = sentence.swapcase()
#         # newSentence = sentence.replace(char, (char.upper()))
#         print('after elif', finalString)
#     else:
#         finalString += char
# print ("The new word is:", finalString)
# vowel_letters = [ c for c in example if c in vowels ]

## Method 2 with pushing to new variable by inverting the vowels using swapcase function
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# sentence = raw_input()
# finalString = ""
# for char in sentence:
#     print('for', char)
#     if char in vowels and char.isupper():
#         print('if', char)
#         finalString += char.swapcase()
#         print('after if', finalString)
#     elif char in vowels and char.islower():
#         print('elif', char)
#         finalString += char.swapcase()
#         print('after elif', finalString)
#     else:
#         finalString += char
# print ("The new word is:", finalString)

## Method 3 with pushing to new variable by inverting the vowels by only checking for vowels
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# sentence = raw_input()
# finalString = ""
# for char in sentence:
#     print('for', char)
#     if char in vowels:
#         print('if', char)
#         finalString += char.swapcase()
#         print('after if', finalString)
#     else:
#         finalString += char
# print ("The new word is:", finalString)

## Method 4 with pushing to new variable by inverting the vowels by checking with ascii values
# Lowercase letters a-z ASCII 97 to 122 
# Uppercase letters A-Z ASCII 65-90
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# sentence = raw_input()
# finalString = ""
# for char in sentence:
#     print(char)
#     if char in vowels and 97<=ord(char)<=122:
#         print(char)
#         finalString += char.swapcase()
#         print ('lower to upper', char)
#     elif char in vowels and 65<=ord(char)<=90:
#         finalString += char.swapcase()
#         print ('upper to lower', char)
#     else:
#         finalString += char
# print ("The new word is:", finalString)


# Problem 3 reverse each cahracter of words in a srtring #
# enter a string
# split the words in a string
# loop through the words in the list
# reverse the words 
# join the reversed words and push to new variable
# print the new string

# example hello world
# olleh dlrow

# sentence = raw_input('Enter a sentance: ')
# finalString = ""
# list = sentence.split()
# for word in list:
#     print(word)
#     word = word[::-1]
#     print(word)
#     finalString = finalString + word + ' '
#     print(finalString)


## Problem 4, reverse a word with each character without using any of the python methods 
# input a string
# find the length of the string
# loop through with range staring from 1
# concate the words in reverse index to a new variable
# print the new string

# sentence = raw_input('Enter a sentance: ')
# finalString = ""
# length = len(sentence)
# for i in range(1, length+1):
#     finalString = finalString + sentence[length-i]
# print('Final string', finalString)

## Problem 4, reverse a word with each character witho using python methods 
# sentence = raw_input('Enter a sentance: ')
# finalString = ""
# for i in range(len(sentence)):
#     # print(i)
#     print (sentence[1:-1])
#     finalString += (sentence[-i-1])
# print('new string', finalString)

## Problem 4, reverse a word with each character without using any of the python methods 
# input a string
# find the length of the string
# loop through with range staring from 1
# concate the words in reverse index to a new variable
# reverse the words 
# concate the reversed words and push to new variable
# print the new string

# example hello
# olleh

# sentence = raw_input('Enter a input: ')
# finalString = ""
# length = len(sentence)

# for i in range(1, length+1):
#     print(i)
#     finalString = finalString + sentence[length-i]
#     print('after', finalString)
# print('Final string', finalString)

## problem 5 prime numbers
# for num in range(1, 1000):
#     for i in range(2, num):
#         if (num%i == 0):
#             break
#     else:
#         print (num)

# if num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")

# lower = input('enter lower input: ')
# upper = input('enter upper input: ')
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num%i == 0):
#                 break
#         else:
#             print ('result', num)


## problem 6, for a word input; increment every letter to the next one
#example 
# input: abc
# output bcd

# word=raw_input("enter a string:")
# final = ""

# for char in word:
#     if (ord(char) == 122):
#         final = chr(ord(char) - 25)
#         print (final)
#     else:
#         final = (chr(ord(char) + 1))
#         print (final)

# with eficient way

# enter the input 
# loop through the string of words
# find the order of the alphabet
# increment the order by one
# print the new alphabet

# value="abz"
# finalOutput=""

# for x in range(len(value)):
#     if ord(value[x]) in range(97,123):
#         finalOutput += (chr(((ord(value[x])-96)%26)+97))
#     elif ord(value[x]) in range(65, 91):
#         finalOutput += (chr(((ord(value[x])-64)%26)+65))
#     else:
#         finalOutput += value[x]
# print (finalOutput)

## same problem with incrementing as user specified

# value = raw_input('Enter a input: ')
# increment = raw_input('Enter a input to increment by: ')
# finalOutput=""

# for x in range(len(value)):
#     if ord(value[x]) in range(97,123):
#         finalOutput = finalOutput + (chr(((ord(value[x])-96)%26)+96+int(increment)))
#     elif ord(value[x]) in range(65, 91):
#         finalOutput = finalOutput + (chr(((ord(value[x])-64)%26)+64+int(increment)))
#     else:
#         finalOutput = finalOutput + value[x]
# print (finalOutput)

## Other way

# value = raw_input('Enter a input: ')
# times = int(input('Enter the number to increment: '))
# finalOutput=""

# for x in range(len(value)):
#     if ord(value[x]) in range(97,123):
#         if times <= 26:
#             smallNum = (((ord(value[x])-96)%26)+96+int(times))
#             if smallNum > 122:
#                 finalOutput = finalOutput + (chr((int(smallNum - 97)%26)+97))
#             else:
#                 finalOutput = finalOutput + (chr(int(smallNum)))
#         else:
#             print ('Please enter below 26')
#     elif ord(value[x]) in range(65, 91):
#         if times <= 26:
#             capNum = (((ord(value[x])-64)%26)+64+int(times))
#             if capNum > 90:
#                 finalOutput = finalOutput + (chr((int(capNum - 65)%26)+65))
#             else:
#                 finalOutput = finalOutput + (chr((int(capNum - 65)%26)+65))
#         else: 
#             print ('Please enter below 26')
#     else:
#         finalOutput = finalOutput + value[x]
# print (finalOutput)

##problem 7, print stars

# value = input('Please enter: ')

# for n in range(0, value):
#     n += 1
#     print ("*", *(n))

# # same problem in reverse order
# for n in range(value, 0, -1):
#     print ("*" *(n))

##problem 8, print stars in triangle pattern

# num = int(input('Enter number of lines '))
# for i in range(1, num+1):
#     print ((num-i)*' '+i*' *')


## Problem 9, 
# A palindrome is a series of characters/numbers read from backwards is same as forwards.
# Accept input
# Find the length
# Reverse the input 
# Loop through each items
# if it's same print TRUE
# word => WOW
# numbers => 121

# value = raw_input('Enter a anything: ')
# length = len(value)
# output = ""

# for i in range(1, length+1):
#     # print ('i',i)
#     output += value[length - i]
#     # print ('out', output)
# if output == value:
#     print (value, 'TRUE It is a Palindrome')
# else:
#     print (value, 'FALSE It is not a Palindrome')

## Python methods 

# reverseVal = value[::-1]
# if reverseVal == value:
#     print (value, 'TRUE It is a Palindrome')
# else:
#     print (value, 'FALSE It is not a Palindrome')

## looping only for the HALF of the input

# value = raw_input('Enter a anything: ')
# length = len(value)
# half = length/2
# first = ""
# output = ""

# for i in range(1, half+1):
#     print ('i', i)
#     first += value[i-length-1]
#     print ('firsthalf', first)
#     output += value[length - i]
#     print ('remaining half', output)

# if output == first:
#     print (value, 'TRUE It is a Palindrome')
# else:
#     print (value, 'FALSE It is not a Palindrome')

## Problem 11, create a dictinary of vowel letter for an input
# accept input
# loop through input 
# find if it's in vowels
# find those vowels in the dictionary
# if it's present increment by 1 or if it's not present set it 1
# print output

## without using python methods
# value = raw_input('Enter a anything: ')
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# output = {}
# # output = {1:'one',2:'two',3:'three'}

# for char in value:
#     if char in vowels:
#         if char in output:
#             output[char] = output[char] + 1
#         else:
#             output[char] = 1
# print ('final', output)

## with python methods
# for char in vowels:
#     print(char)
#     count = string.count(char)
#     if count >= 1:
#         output[char]= count
# print (output)

##problem 12, decimal to hexadecimal conversion
# input
# divide the input by 16, divide the quotient till the remainder becomes zero.
# then join the qutioent and remainders = hexa if remainder is more than 10 => use hexa values A=10B=11C=12D=13E=14F=15


# num = int(input("Enter a decimal number: "))
# output = ""
# lastRemainder = []

# if (num < 0):
#     print ('wrong input')
# elif (num == 0):
#     print ('please enter a valid number')
# else:
#     if (num > 16):
#         quotient = (num / 16)
#         remainder = (num % 16)

#         if quotient >= 16:
#             while quotient >= 16 or remainder == 0:
#                 if quotient >= 16:
#                     lastQuotient = (quotient/16)
#                     remainder = (quotient % 16)
#                     quotient = lastQuotient
#                     lastRemainder.append(remainder)
#             lastRemainder.reverse()
#             output = (lastQuotient,lastRemainder)
#         else:
#             output = (quotient,remainder)

#     elif (num == 16):
#         quotient = (num / 16)
#         remainder = (num % 16)
#         output = (quotient,remainder)
#     else:
#         quotient = num
#         output = (quotient)

#     print ('the hexadecimal is', output)


# if (num < 0):
#     print ('wrong input')
# elif (num == 0):
#     print ('please enter a valid number')
# else:
#     quotient = (num / 16) #get quotient
#     remainder = (num % 16) #get remainder
#     lastRemainder.append(remainder)

#     while quotient >= 16 or remainder == 0:
#         if quotient >= 16:
#             lastQuotient = (quotient/16)
#             remainder = (quotient % 16)
#             quotient = lastQuotient
#             lastRemainder.append(remainder)
#     lastRemainder.reverse()
#     output = (lastQuotient,lastRemainder)
#     print ('the hexadecimal is', output)


# ## with single while loop

# num = int(input("Enter a decimal number: "))
# output = ""
# lastRemainder = []

# if (num < 0):
#     print ('wrong input')
# elif (num == 0):
#     print ('please enter a valid number')
# else:
#     if (num > 16):
#         quotient = (num / 16)
#         remainder = (num % 16)
#         lastRemainder.append(remainder)
#         if quotient >= 16:
#             while quotient >= 16:
#                 lastQuotient = (quotient/16)
#                 remainder = (quotient % 16)
#                 quotient = lastQuotient
#                 lastRemainder.append(remainder)
#             lastRemainder.reverse()
#             output = (lastQuotient,lastRemainder)
#         else:
#             output = (quotient,remainder)

#     elif (num == 16):
#         quotient = (num / 16)
#         remainder = (num % 16)
#         output = (quotient,remainder)
#     else:
#         quotient = num
#         output = (quotient)
#     print ('the hexadecimal is', output)

## with multiple while loop

# num = int(input("Enter a decimal number: "))
# output = ""
# lastRemainder = []

# if (num < 0):
#     print ('wrong input')
# elif (num == 0):
#     print ('please enter a valid number')
# else:
#     if (num > 16):
#         quotient = (num / 16)
#         remainder = (num % 16)
#         lastRemainder.append(remainder)
#         if quotient >= 16:
#             while quotient >= 16:
#                 lastQuotient = (quotient/16)
#                 remainder = (quotient % 16)
#                 quotient = lastQuotient
#                 lastRemainder.append(remainder)
#             lastRemainder.reverse()
#             output = (lastQuotient,lastRemainder)
#         # elif quotient == 16 or remainder == 0:
#         #     while quotient == 16 or remainder == 0:
#         #         print ('=== 16', quotient)
#         #         print ('=== 16', remainder)
#         #         lastQuotient = (quotient/16)
#         #         remainder = (quotient % 16)
#         #         quotient = lastQuotient
#         #         lastRemainder.append(remainder)
#         #         break
#         #     lastRemainder.reverse()
#         #     output = (lastQuotient,lastRemainder)
#         #     print ('el if output', output)
#         else:
#             output = (quotient,remainder)

#     elif (num == 16):
#         quotient = (num / 16)
#         remainder = (num % 16)
#         output = (quotient,remainder)
#     else:
#         quotient = num
#         output = (quotient)
#     print ('the hexadecimal is', output)



## with all BASE
# BASE = 16
# num = int(input("Enter a decimal number: "))
# hexadecimal = []

# if (num < 0):
#     print ('wrong input')
# elif (num == 0):
#     print ('please enter a valid number')
# else:
#     if (num > BASE):
#         quotient = (num / BASE)
#         remainder = (num % BASE)

#         hexadecimal.append(remainder)

#         if quotient >= BASE:
#             while quotient >= BASE:
#                 lastQuotient = (quotient/BASE)
#                 remainder = (quotient % BASE)
#                 quotient = lastQuotient
#                 hexadecimal.append(remainder)

#             hexadecimal.reverse()
#             hexadecimal.insert(0, lastQuotient)

#         else:
#             hexadecimal.append(quotient)
#             hexadecimal.append(remainder)

#     elif (num == BASE):
#         quotient = (num / BASE)
#         remainder = (num % BASE)

#         hexadecimal.append(quotient)
#         hexadecimal.append(remainder)

#     else:
#         hexadecimal.append(num)

#     print ('the hexadecimal is', hexadecimal)

#     for num in hexadecimal:
#         if (num == 10):
#             print "A",
#         elif (num == 11):
#             print "B",
#         elif (num == 12):
#             print "C",
#         elif (num == 13):
#             print "D",
#         elif (num == 14):
#             print "E",
#         elif (num == 15):
#             print "F",
#         else:
#             print num,



## problem 13, hexadecimal to decimal conversion

## decimal to hexadecimal 
# input
# divide the input by 16, divide the quotient till the remainder becomes zero.
# then join the qutioent and remainders = hexa if remainder is more than 10 => use hexa values A=10B=11C=12D=13E=14F=15

# BASE = 16
# hexa = raw_input("Enter a hexadecimal number: ")
# decimalValues = []
# indexes = []
# multiplied = []
# decimalReversed = []
# decimalOutput = 0

# for digi in hexa:
#     if (digi == "A"):
#         decimalValues.append(10),
#     elif (digi == "B"):
#         decimalValues.append(11),
#     elif (digi == "C"):
#         decimalValues.append(12),
#     elif (digi == "D"):
#         decimalValues.append(13),
#     elif (digi == "E"):
#         decimalValues.append(14),
#     elif (digi == "F"):
#         decimalValues.append(15),
#     else:
#         decimalValues.append(digi),

# length = len(decimalValues)
# # print ('converted to decimal base value', decimalValues)

# for x in range(0, length):
#     indexes.append(x)
#     multiplied.append(BASE**indexes[x])
# # print ('index values', indexes)
# # print ('multiplied', multiplied)

# for x in range(1, length+1):
#     decimalReversed = decimalReversed + [str(decimalValues[length-x])]
# # print ('Decimals in reverse order', decimalReversed)

# # for y in indexes:
# #     multiplied.append(BASE**y)
# # print ('multiplied 16 with indexes', multiplied)

# for i in range(len(decimalReversed)):
#     decimalReversed[i] = ((int(decimalReversed[i])) * (int(multiplied[i])))
#     decimalOutput = decimalOutput + decimalReversed[i]
# # print ('multiplied the reverse decimal values with 16 indexes', decimalReversed)

# # for item in decimalReversed:
# #     decimalOutput = decimalOutput + item

# print ('The Decimal value of the input is', decimalOutput)


### with more loop reduced 
# BASE = 16
# hexa = raw_input("Enter a hexadecimal number: ")
# decimalValues = []
# indexes = []
# multiplied = []
# decimalReversed = []
# decimalOutput = 0

# for digi in hexa:
#     if (digi == "A"):
#         decimalValues.append(10),
#     elif (digi == "B"):
#         decimalValues.append(11),
#     elif (digi == "C"):
#         decimalValues.append(12),
#     elif (digi == "D"):
#         decimalValues.append(13),
#     elif (digi == "E"):
#         decimalValues.append(14),
#     elif (digi == "F"):
#         decimalValues.append(15),
#     else:
#         decimalValues.append(digi),

# length = len(decimalValues)
# print ('converted to decimal base value', decimalValues)

# for x in range(0, length):
#     indexes.append(x)
#     multiplied.append(BASE**indexes[x])
# print ('index values', indexes)
# print ('multiplied', multiplied)


# for i in range(0, len(hexa)):
#     digi = hexa[i]
#     if (digi == "A"):
#         decimalValues.append(10),
#     elif (digi == "B"):
#         decimalValues.append(11),
#     elif (digi == "C"):
#         decimalValues.append(12),
#     elif (digi == "D"):
#         decimalValues.append(13),
#     elif (digi == "E"):
#         decimalValues.append(14),
#     elif (digi == "F"):
#         decimalValues.append(15),
#     else:
#         decimalValues.append(int(digi)),
    
#     indexes.append(range(0, len(hexa)))
    # print ('digi', indexes)
    # print ('digi', i)

#     multiplied.append(BASE**i)
# print (' multiplied digi', multiplied)

# print ('decimalValues', decimalValues)

# length = len(decimalValues)

# for x in range(1, length+1):
#     decimalReversed = decimalReversed + [str(decimalValues[length-x])]
# # print ('Decimals in reverse order', decimalReversed)

# for y in indexes:
#     multiplied.append(BASE**y)
# print ('multiplied 16 with indexes', multiplied)

# length1 = len(decimalValues)
# for i in range(length1):
#     temp = decimalValues[length1-1-i] *  multiplied[i]
#     print ('temp', temp)
#     decimalOutput = decimalOutput + temp

    # decimalReversed[i] = ((int(decimalReversed[i])) * (int(multiplied[i])))
    # decimalOutput = decimalOutput + decimalReversed[i]
# print ('multiplied the reverse decimal values with 16 indexes', decimalReversed)

# for item in decimalReversed:
#     decimalOutput = decimalOutput + item


# print ('The Decimal value of the input is', decimalOutput)

### cleaner code 
# BASE = 16
# hexa = raw_input("Enter a hexadecimal number: ")
# decimalValues = []
# indexes = []
# multiplied = []
# decimalOutput = 0
# A = 10
# finalInput = ""
# for i in hexa:
#     if i in decimalNumbers:
#         finalInput = finalInput + i
#     elif ord(i) in range(65,70):
#         finalInput = finalInput + i
#     elif ord(i) in range(97,102):
#         finalInput += i.swapcase()
#     else:
#         print ('please enter proper input')

# for i in range(0, len(finalInput)):
#     digi = finalInput[i]

#     if digi not in decimalNumbers:
#         some = A + (ord(digi) - ord('A'))
#         decimalValues.append(some)
#     else:
#         decimalValues.append(int(digi))
    
#     indexes.append(range(0, len(finalInput)))

#     multiplied.append(BASE**i)

# length = len(decimalValues)

# for i in range(length):
#     temp = decimalValues[length-1-i] *  multiplied[i]
#     decimalOutput = decimalOutput + temp

# print ('The Decimal value of the input is', decimalOutput)


#### same problem with more python way and input validation checks

# decimalNumbers = ['0','1','2','3','4','5','6','7','8','9']

# decimalValues = []
# indexes = []
# multiplied = []
# A = 10

# def validateInput(base, inputString):
#     symbol_start_upper = 65
#     symbol_end_upper = symbol_start_upper + (base-10)

#     symbol_start_lower = 97
#     symbol_end_lower = symbol_start_lower + (base-10)

#     for i in inputString:
#         if i in decimalNumbers:
#             # The char is valid, check next char
#             continue
#         elif ord(i) in range(symbol_start_upper,symbol_end_upper):
#             # The char is valid, check next char
#             continue
#         elif ord(i) in range(symbol_start_lower,symbol_end_lower):
#             # The char is valid, check next char
#             continue
#         else:
#             # The char is invalid, return False
#             return False
#     return True

# def convertNumber(base, inputNumber, targetBase):
#     finalInput = inputNumber.upper()
#     decimalOutput = 0

#     for i in range(0, len(finalInput)):
#         digi = finalInput[i]

#         if digi not in decimalNumbers:
#             some = A + (ord(digi) - ord('A'))
#             decimalValues.append(some)
#         else:
#             decimalValues.append(int(digi))
        
#         indexes.append(range(0, len(finalInput)))

#         multiplied.append(base**i)

#     length = len(decimalValues)

#     for i in range(length):
#         temp = decimalValues[length-1-i] *  multiplied[i]
#         decimalOutput = decimalOutput + temp
#     return decimalOutput

# def deciToTarget(base, decimalOutput):
#     num = decimalOutput
#     originalInput = []
#     convertedNumber = []

#     q = num / base
#     r = num % base
#     originalInput.append(r)

#     if (q >= base):
#         while q >= base:
#             lastQuotient = (q/base)
#             r = (q % base)
#             q = lastQuotient
#             originalInput.append(r)

#         originalInput.reverse()
#         originalInput.insert(0, lastQuotient)

#     for num in originalInput:
#         if (num == 10):
#             convertedNumber.append("A"),
#         elif (num == 11):
#             convertedNumber.append("B"),
#         elif (num == 12):
#             convertedNumber.append("C"),
#         elif (num == 13):
#             convertedNumber.append("D"),
#         elif (num == 14):
#             convertedNumber.append("E"),
#         elif (num == 15):
#             convertedNumber.append("F"),
#         else:
#             convertedNumber.append(num),

#     return convertedNumber

# if __name__ == '__main__':

#     base = int(raw_input("Enter base for the number: "))
#     inputNumber = raw_input("Enter the number: ")
#     if validateInput(base, inputNumber):
#         print("Valid number")
#         targetBase = int(raw_input("Enter target base for the number: "))
#         decimalOutput = convertNumber(base, inputNumber, targetBase)
#         print ('The Decimal value of the input is', decimalOutput)
#         convertedNumber = deciToTarget(base, decimalOutput)
#         print ('Your original input was', convertedNumber)
#     else:
#         print("Invalid number")

#### same prob, with both way conversion

# decimalNumbers = ['0','1','2','3','4','5','6','7','8','9']

# decimalValues = []
# indexes = []
# multiplied = []
# A = 10

# def validateInput(base, inputString):
#     symbol_start_upper = 65
#     symbol_end_upper = symbol_start_upper + (base-10)

#     symbol_start_lower = 97
#     symbol_end_lower = symbol_start_lower + (base-10)

#     for i in inputString:
#         if i in decimalNumbers:
#             # The char is valid, check next char
#             continue
#         elif ord(i) in range(symbol_start_upper,symbol_end_upper):
#             # The char is valid, check next char
#             continue
#         elif ord(i) in range(symbol_start_lower,symbol_end_lower):
#             # The char is valid, check next char
#             continue
#         else:
#             # The char is invalid, return False
#             return False
#     return True

# def convertNumber(base, inputNumber, targetBase):
#     finalInput = inputNumber
#     decimalOutput = 0

#     for i in range(0, len(finalInput)):
#         digi = finalInput[i]

#         if digi not in decimalNumbers:
#             some = A + (ord(digi) - ord('A'))
#             decimalValues.append(some)
#         else:
#             decimalValues.append(int(digi))
        
#         indexes.append(range(0, len(finalInput)))

#         multiplied.append(base**i)

#     length = len(decimalValues)

#     for i in range(length):
#         temp = decimalValues[length-1-i] *  multiplied[i]
#         decimalOutput = decimalOutput + temp

#     return decimalOutput

# def deciToTarget(targetBase, decimalOutput):
#     num = decimalOutput
#     originalInput = []
#     convertedNumber = []
#     base = targetBase
#     targetOuput = ''

#     q = num / base
#     r = num % base
#     originalInput.append(r)

#     if (q >= base):
#         while q >= base:
#             lastQuotient = (q/base)
#             r = (q % base)
#             q = lastQuotient
#             originalInput.append(r)

#         originalInput.reverse()
#         originalInput.insert(0, lastQuotient)

#     for num in originalInput:
#         if num > 9:
#             symbol = chr(65 + (num - 10))
#             convertedNumber.append(symbol)
#         else:
#             convertedNumber.append(num)

#     for s in convertedNumber:
#         targetOuput = targetOuput + str(s)

#     return targetOuput


# base = int(raw_input("Enter base for the number: "))
# inputNumber = raw_input("Enter the number: ")
# if validateInput(base, inputNumber):
#     print("Valid number")
#     targetBase = int(raw_input("Enter target base for the number: "))
#     decimalOutput = convertNumber(base, inputNumber, targetBase)
#     print ('The Decimal value of the input is', decimalOutput)
#     targetOuput = deciToTarget(targetBase, decimalOutput)
#     print ('Your original input was', targetOuput)
# else:
#     print("Invalid number")
