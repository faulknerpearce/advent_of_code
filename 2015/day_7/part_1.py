
def read_file(file):
    instructions = []
    with open(file) as data:
        for line in data.readlines():
            instructions.append(line.split())

    return instructions

def follow_instruction(lines):

    for line in lines:

        for element in line:

            if ord(element[0]) >= 48 and ord(element[0]) <= 57:
                print(f'{element}. is a number')

            elif ord(element[0]) >= 97 and ord(element[0]) <= 122:
                print(f'{element}. is a string')
        
            else:
                print(f'{element}. is a command.')
        print()
   
# my_instructions = read_file('test.txt')

# follow_instruction(my_instructions)