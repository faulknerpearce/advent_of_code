def read_file_return_2d_list(file):
    '''Reads the input file and returns its content as a 2D matrix.'''
    with open(file) as data:
        array = [list(line.strip('\n')) for line in data.readlines()]

        return array
    
def get_antenna_locations(matrix):
    '''Identifies the positions of all antennas in the grid and groups them by frequency.'''
    loc_dict = {}

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != '#' and matrix[row][col] != '.':
                if loc_dict.get(matrix[row][col]):
                    loc_dict[matrix[row][col]].add((row, col))
                else:
                    loc_dict.update({matrix[row][col]: {(row, col)}})

    return loc_dict

def add_anti_nodes(antenna_a, antenna_b, anti_nodes, matrix):
    '''Calculates and adds anti nodes based on the alignment of a pair of antennas.'''
    antenna_ax, antenna_ay = antenna_a
    antenna_bx, antenna_by = antenna_b

    distance_x = antenna_bx - antenna_ax
    distance_y = antenna_by - antenna_ay

    antinode1 = (antenna_ax - distance_x, antenna_ay - distance_y)
    antinode2 = (antenna_bx + distance_x, antenna_by + distance_y)

    if 0 <= antinode1[0] < len(matrix) and 0 <= antinode1[1] < len(matrix[0]):
        if matrix[antinode1[0]][antinode1[1]] != '#':
            anti_nodes.add(antinode1)

    if 0 <= antinode2[0] < len(matrix) and 0 <= antinode2[1] < len(matrix[0]):
        if matrix[antinode2[0]][antinode2[1]] != '#':
            anti_nodes.add(antinode2)
         

    return anti_nodes

def part_one(loc_dict, matrix):
    '''Processes all pairs of antennas with the same frequency and calculates the number of anti nodes.'''
    connected = set()
    anti_nodes = set()

    for key in loc_dict.keys():

        for antenna in loc_dict[key]:
            connected.add(antenna)

            for next_antenna in loc_dict[key]:
                if next_antenna != antenna and next_antenna not in connected:
                    anti_nodes = add_anti_nodes(antenna, next_antenna, anti_nodes, matrix)

    return len(anti_nodes)
    
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    antenna_locations = get_antenna_locations(puzzle_input)

    answer = part_one(antenna_locations, puzzle_input)

    print(f'The answer to part one is: {answer}')
