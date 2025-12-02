import re 

# Parse the input file and return a list of range pairs
def read_file_return_list(file):
    with open(file) as file_raw:

        data = re.sub(r'\n|,', ' ', file_raw.read())

        return [text.split('-') for text in data.split()]

# Split an ID into two equal halves
def split_in_half(num):
    num_list = list(num)
    mid = len(num) // 2

    return ''.join(num_list[:mid]), ''.join(num_list[mid:])
  
# Find all IDs in the range where the first half equals the second half  
def get_invalid_ids(start, stop):
    invalid_ids = []

    for i in range(int(start), (int(stop) +1)):
        str_num = str(i)
        
        if len(str_num) % 2 == 0:
            num_a, num_b = split_in_half(str_num)

            if num_a == num_b:
                id = ''.join(num_a + num_b)
                
                invalid_ids.append(int(id))

    return invalid_ids

# Process all instruction ranges and calculate the sum of invalid IDs
def part_one(instructions):
    invalid_ids = []

    for instruction in instructions:

        new_ids = get_invalid_ids(instruction[0], instruction[1])

        if new_ids:
            invalid_ids += new_ids

    return sum(invalid_ids)


# Event: https://adventofcode.com/2025/day/2
if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
    