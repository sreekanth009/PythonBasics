from base_converter import validateInput, convertNumber, deciToTarget

def get_input_list():
    current_input_list = []
    current_individual_input = []

    while True:
        current_input = raw_input("Enter base, input and targetBase: ")
        if current_input == "":
            break
        else:
            current_input_list.append(current_input)

    for element in current_input_list:
        parts = element.split(',')

        the_input_dict = {
            'base': int(parts[0]),
            'input': parts[1],
            'targetBase': int(parts[2])
        }
        current_individual_input.append(the_input_dict)

    return current_individual_input

def process_input_list(current_individual_input):
    result_list = []
    for i in current_individual_input:
        # print ('processing input', i['input'])
        isValid = validateInput(i['base'], i['input'])
        if isValid:
            # print("Valid number")
            decimalOutput = convertNumber(i['base'], i['input'], i['targetBase'])
            # print ('The Decimal value of the input is', decimalOutput)
            targetOuput = deciToTarget(i['targetBase'], decimalOutput)
            # print ('The output of target base', targetOuput)

            result_list.append(targetOuput)

        else:
            # print("Invalid number")
            result_list.append(isValid)

    return result_list

if __name__ == '__main__':
    inputlist = get_input_list()
    outputs = process_input_list(inputlist)
    for output in outputs:
        if output:
            print(output)
        else:
            print('invalid input')
