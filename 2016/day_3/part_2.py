from part_1 import read_file_return_2D_list, is_triangle

def count_valid_triangles_by_column(instructions):
    '''Counts the number of valid triangles in the given instructions by columns, where each set of three rows forms a triangle.'''
    total = 0

    for col in range(3):
        for row in range(0, len(instructions), 3):

            a = instructions[row][col]
            b = instructions[row+1][col]
            c = instructions[row+2][col]

            if is_triangle(a, b, c):
                total += 1
    return total

# Event: https://adventofcode.com/2016/day/3
if __name__ == '__main__':

    puzzle_input = read_file_return_2D_list('text.txt')

    answer = count_valid_triangles_by_column(puzzle_input)

    print(f'The answer to part two is: {answer}')
