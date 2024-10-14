from part_1 import convert_sequence

# Repeats the conversion process 50 times and returns the length of the final sequence
def part_one(numbers):
    for _ in range(50):
        numbers = convert_sequence(numbers)

    return (len(numbers))

if __name__ == '__main__':

    puzzle_input = '1113222113'

    answer = part_one(puzzle_input)
    
    print(f'The answer to part two is: {answer}')