from part_1 import read_file_return_list, rotate

def count_during_rotations(current_position, amount, direction):
    count = 0 
    delta = -1 if direction == 'L' else 1

    for _ in range(int(amount)):
        current_position = (current_position + delta) % 100
        if current_position == 0:
            count += 1

    return count

def part_two(instructions):
    count = 0
    dial_position = 50

    for instruction in instructions:
        
        count += count_during_rotations(dial_position, instruction[1:], instruction[0])
        dial_position = rotate(dial_position, instruction[1:], instruction[0])

    return count

if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')