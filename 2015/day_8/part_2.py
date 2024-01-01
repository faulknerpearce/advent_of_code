from part_1 import read_file_return_list

# This function will count characters in code versus characters in memory for string literals
def count_encoded_literals(text):
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

#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = count_encoded_literals(puzzle_input)

    print(f'The answer to part two is: {answer}')


