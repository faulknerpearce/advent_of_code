# Reads a file and returns two lists of integers split from each line.
def read_file_return_two_lists(file):
    left = []
    right = []

    with open(file) as data:
        text = data.readlines()

        for line in text:  
          
          nums = line.split()
          left.append(int(nums[0]))
          right.append(int(nums[1]))

    return left, right
             
# Calculates the total of absolute differences between pairs of smallest numbers from two lists.
def part_one(left_array, right_array):
    total = 0

    left_array.sort()
    right_array.sort()

    for i in range(len(left_array)):

        total += abs(left_array[i] - right_array[i])

    return total

if __name__ == '__main__':

    left_side, right_side = read_file_return_two_lists('text.txt')

    answer = part_one(left_side, right_side)

    print(f'The answer to part one is: {answer}')