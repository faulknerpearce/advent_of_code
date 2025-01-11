from part_1 import convert_sequence

def part_one(numbers):
    '''Repeats the conversion process 50 times and returns the length of the final sequence'''
    for _ in range(50):
        numbers = convert_sequence(numbers)

    return (len(numbers))

# Event: https://adventofcode.com/2015/day/10
if __name__ == '__main__':

    puzzle_input = '1113222113'

    answer = part_one(puzzle_input)
    
    print(f'The answer to part two is: {answer}')