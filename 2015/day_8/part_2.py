from part_1 import read_file_return_list

def part_two(text):
    '''Counts characters in code versus characters in memory for string literals'''
    total_encoded_chars = 0
    total_string_code = 0

    for input_str in text:
        total_string_code += len(input_str)
        encoded_chars = 2 

        for char in input_str:
            if char == '\\' or char == '"':
                encoded_chars += 2  
            else:
                encoded_chars += 1  
        total_encoded_chars += encoded_chars

    result = total_encoded_chars - total_string_code
    return result

# Event: https://adventofcode.com/2015/day/8
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')


