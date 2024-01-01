from part_1 import read_file_return_2D_list

# Counts the number of valid triangles formed by vertical columns in three rows
def count_triangles(row_one, row_two, row_three):
    count = 0
    for i in range(3):
        if (row_one[i] + row_two[i] > row_three[i]) and (row_one[i] + row_three[i] > row_two[i]) and (row_two[i] + row_three[i] > row_one[i]):
            count += 1
    return count

# Calculates the total count of valid triangles when considering columns of three consecutive rows
def get_possible_triangle_columns(lines):
    valid_count = 0
    for row in range(0, len(lines), 3):
        row_a, row_b, row_c = lines[row], lines[row+1], lines[row+2]
        valid_count += count_triangles(row_a, row_b, row_c)  
    return valid_count 

#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_2D_list('text.txt')

    answer = get_possible_triangle_columns(puzzle_input)

    print(f'The answer to part two is: {answer}')
