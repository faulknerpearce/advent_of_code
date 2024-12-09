from part_1 import read_file_return_two_lists

# Calculates the total product based on occurrences of left_array elements in right_array.
def part_two(left_array, right_array):
    results = {}
    total = 0

    for i in range(len(left_array)):

        if results.get(left_array[i]):
            total += results[left_array[i]]

        else:
            right_count = right_array.count(left_array[i])
            
            product = left_array[i] * right_count
            
            results.update({left_array[i]: product})

            total += product

    return total

# Event: https://adventofcode.com/2024/day/1
if __name__ == '__main__':
    
    left_side, right_side = read_file_return_two_lists('text.txt')

    answer = part_two(left_side, right_side)

    print(f'The answer to part two is: {answer}')