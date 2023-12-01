import re

def read_file(file):
    with open(file) as data:
        text = data.read().splitlines()
    return text

def find_double_quote(line):
    minus = 0
    for char in line:
        if char == '"':
            minus += 1
    return minus

def find_escape_character(line):
    minus = 0
    for i in range(len(line)):
        if line[i] == '\\':
            if line[i+1] == 'x':
                minus += 3
            else:
                minus = 1
    return minus

def count_total_memory(text):
    string_literal = 0
    string_memory = 0

    for line in text:
        string_literal += len(line)
        string_memory += find_double_quote(line)
        string_memory += find_escape_character(line)

    total = string_literal - string_memory

    print(f'The Total literal characters were: {string_literal} The total in memory was: {string_memory} The result was: {total}')

my_text = read_file('text.txt')
count_total_memory(my_text)