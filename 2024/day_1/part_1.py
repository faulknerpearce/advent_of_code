def read_file_return_two_lists(file):
    '''Reads a file and returns two lists of integers split from each line.'''
    left = []
    right = []

    with open(file) as data:
        text = data.readlines()

        for line in text:  
          nums = line.split()

          left.append(int(nums[0]))
          right.append(int(nums[1]))

    return left, right
             
def part_one(left_array, right_array):
    '''Calculates the total of absolute differences between pairs of sorted numbers from two lists.'''
    total = 0

    left_array.sort()
    right_array.sort()

    for i in range(len(left_array)):
        total += abs(left_array[i] - right_array[i])

    return total

# Event: https://adventofcode.com/2024/day/1
if __name__ == '__main__':

    left_side, right_side = read_file_return_two_lists('text.txt')

    answer = part_one(left_side, right_side)

    print(f'The answer to part one is: {answer}')