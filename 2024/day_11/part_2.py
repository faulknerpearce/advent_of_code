from part_1 import read_file_return_dict, transform_stones

def part_one(stones, blinks):
    '''Repeatedly transform stones; 75 times.'''
    for _ in range(blinks):
        stones = transform_stones(stones)

    return sum(stones.values())

# Event: https://adventofcode.com/2024/day/11
if __name__ == '__main__':
   
    puzzle_input = read_file_return_dict('text.txt')
    
    answer = part_one(puzzle_input, 75)
    
    print(f'The answer to part one is: {answer}')
