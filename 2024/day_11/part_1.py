def read_file_return_dict(file):
    '''Reads a file and returns a frequency dictionary of stone values.'''
    stones = {}

    with open(file) as data:
        for num in data.read().split():
            value = int(num)
            stones[value] = stones.get(value, 0) + 1

    return stones

def split_stone(value, count, stones):
    '''Splits a stone into two halves, removes leading zeros, and updates their frequencies in the map.'''
    mid = len(value) // 2
            
    left = int(value[:mid].lstrip('0') or '0')
    right = int(value[mid:].lstrip('0') or '0')

    stones[left] = stones.get(left, 0) + count
    stones[right] = stones.get(right, 0) + count

    return stones

def transform_stones(stones):
    '''single 0 digits are replaced by 1; even digits split into two halves; odd digits multiply by 2024.'''
    transformed_stones = {}

    for value, count in stones.items():
        value_str = str(value)  

        if value == 0:
            transformed_stones[1] = transformed_stones.get(1, 0) + count

        elif len(value_str) % 2 == 0:
            transformed_stones = split_stone(value_str, count, transformed_stones)
         
        else:
            transformed_value = value * 2024
            transformed_stones[transformed_value] = transformed_stones.get(transformed_value, 0) + count

    return transformed_stones

def part_one(stones, blinks):
    '''Repeatedly transform stones; 25 times.'''
    for _ in range(blinks):
        stones = transform_stones(stones)

    return sum(stones.values())

# Event: https://adventofcode.com/2024/day/11
if __name__ == '__main__':

    puzzle_input = read_file_return_dict('text.txt')

    answer = part_one(puzzle_input, 25)

    print(f'The answer to part one is: {answer}')

