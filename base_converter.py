## decimal to hexadecimal 
# input
# divide the input by 16, divide the quotient till the remainder becomes zero.
# then join the qutioent and remainders = hexa if remainder is more than 10 => use hexa values A=10B=11C=12D=13E=14F=15

decimalNumbers = ['0','1','2','3','4','5','6','7','8','9']

decimalValues = []
indexes = []
multiplied = []
A = 10

def validateInput(base, inputString):
    symbol_start_upper = 65
    symbol_end_upper = symbol_start_upper + (base-10)

    symbol_start_lower = 97
    symbol_end_lower = symbol_start_lower + (base-10)

    for i in inputString:
        if i in decimalNumbers:
            # The char is valid, check next char
            continue
        elif ord(i) in range(symbol_start_upper,symbol_end_upper):
            # The char is valid, check next char
            continue
        elif ord(i) in range(symbol_start_lower,symbol_end_lower):
            # The char is valid, check next char
            continue
        else:
            # The char is invalid, return False
            return False
    return True

def convertNumber(base, inputNumber, targetBase):
    finalInput = inputNumber.upper()
    decimalOutput = 0

    for i in range(0, len(finalInput)):
        digi = finalInput[i]

        if digi not in decimalNumbers:
            some = A + (ord(digi) - ord('A'))
            decimalValues.append(some)
        else:
            decimalValues.append(int(digi))
        
        indexes.append(range(0, len(finalInput)))

        multiplied.append(base**i)

    length = len(decimalValues)

    for i in range(length):
        temp = decimalValues[length-1-i] *  multiplied[i]
        decimalOutput = decimalOutput + temp

    return decimalOutput

def deciToTarget(targetBase, decimalOutput):
    num = decimalOutput
    originalInput = []
    convertedNumber = []
    base = targetBase
    targetOuput = ''

    q = num / base
    r = num % base
    originalInput.append(r)

    if (q >= base):
        while q >= base:
            lastQuotient = (q/base)
            r = (q % base)
            q = lastQuotient
            originalInput.append(r)

        originalInput.reverse()
        originalInput.insert(0, lastQuotient)

    for num in originalInput:
        if num > 9:
            symbol = chr(65 + (num - 10))
            convertedNumber.append(symbol)
        else:
            convertedNumber.append(num)

    for s in convertedNumber:
        targetOuput = targetOuput + str(s)

    return targetOuput

if __name__ == '__main__':

    base = int(raw_input("Enter base for the number: "))
    inputNumber = raw_input("Enter the number: ")
    if validateInput(base, inputNumber):
        print("Valid number")
        targetBase = int(raw_input("Enter target base for the number: "))
        decimalOutput = convertNumber(base, inputNumber, targetBase)
        print ('The Decimal value of the input is', decimalOutput)
        targetOuput = deciToTarget(targetBase, decimalOutput)
        print ('Your original input was', targetOuput)
    else:
        print("Invalid number")

