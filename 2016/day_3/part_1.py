def read_file_return_2D_list(file):
    '''Reads a file and returns its content as a 2D list.'''
    with open(file) as text:
        instructions = [line.split() for line in text.readlines()]
    return instructions

def is_triangle(a, b, c):
    '''Checks if three given sides can form a valid triangle.'''
    return (int(a) + int(b)) > int(c) and (int(b) + int(c)) > int(a) and (int(c) + int(a)) > int(b)

def count_valid_triangles_by_row(instructions):
    '''Counts the number of valid triangles in the given instructions, where each row represents a triangle.'''
    total = 0 

    for instruction in instructions:
        if is_triangle(instruction[0], instruction[1], instruction[2]):
            total += 1
    return total 

# Event: https://adventofcode.com/2016/day/3
if __name__ == '__main__':
    
    puzzle_input = read_file_return_2D_list('text.txt')

    answer = count_valid_triangles_by_row(puzzle_input)

    print(f'The answer to part one is: {answer}')
    