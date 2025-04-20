from part_1 import read_file_return_list, get_error_corrected_message

# Event: https://adventofcode.com/2016/day/6
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = get_error_corrected_message(puzzle_input, False)

    print(f'The answer to part two is: {answer}')