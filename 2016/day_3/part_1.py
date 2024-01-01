# Reads a file and returns a 2D array of numbers.
def read_file_return_2D_list(file, lines=[]):
    with open(file) as data:
        for line in data:
            nums = [int(num) for num in line.split()]
            lines.append(nums)
    return lines

# Counts the number of valid triangles by row in an arry.
def get_possible_triangle_rows(lines):
    count = 0
    for line in lines:
        a, b, c = line[0], line[1], line[2]
        if (a + b > c) and (a + c > b) and (b + c > a):
            count += 1
    return count

#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_2D_list('text.txt')

    answer = get_possible_triangle_rows(puzzle_input)

    print(f'The answer to part one is: {answer}')

