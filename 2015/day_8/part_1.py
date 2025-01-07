def read_file_return_list(file):
    '''Read text from a file and return a list of strings.'''
    with open(file) as data:
        text = data.read().splitlines()
    return text

def part_one(text):
    '''Count characters in code versus characters in memory for string literals'''

    total_string_code = 0
    total_mem_chars = 0

    for input_str in text:
        total_string_code += len(input_str)
        chars = iter(input_str)
        mem_chars = 0

        for char in chars:
            
            if char == '\\':
                next_char = next(chars)
                if next_char == 'x':
                    next(chars)
                    next(chars)
            mem_chars += 1

        total_mem_chars += mem_chars - 2

    result = total_string_code - total_mem_chars
    return result 

#________Main Program_________ # 
if __name__ == "__main__":
    
    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')

