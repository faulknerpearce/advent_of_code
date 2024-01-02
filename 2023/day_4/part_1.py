import re

def read_file_and_create_list(file):
    with open(file) as data:
        text = data.read()
        formatted = re.sub(r'Card|:|', '', text)
        lines = formatted.split('\n')
        
        my_list = [line.split() for line in lines]
    return my_list

puzzle_input = read_file_and_create_list('text.txt')

print(puzzle_input)