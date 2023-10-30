'''Day seven part one of advent of code.'''

def read_file():
    '''This reads instructions from a text file and appends each step to a list of instructions'''
    instructons = []
    with open('test.txt', encoding='utf-8') as file:
        for _ in file.readline():
            instructons.append(file.readline().split())
    return instructons

my_instructions = read_file()
print(my_instructions)
