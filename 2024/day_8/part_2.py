from part_1 import read_file_return_2d_list, get_antenna_locations

def in_bounds(antinode, matrix):
    """Checks if the given position is within bounds of the matrix."""
    return 0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0])

def add_all_anti_nodes(antinode, dx, dy, anti_nodes, matrix):
    """Adds anti nodes extending outward in the given direction until out of bounds."""
    while True:
        antinode = (antinode[0] + dx, antinode[1] + dy)
        if in_bounds(antinode, matrix):
            anti_nodes.add(antinode)
        else:
            break

    return anti_nodes

def get_starting_position(antinode, dx, dy, matrix):
    """Finds the farthest valid starting position in the given direction."""
   
    while in_bounds(antinode, matrix):
        antinode = (antinode[0] - dx, antinode[1] - dy)
   
    return (antinode[0] + dx, antinode[1] + dy)

def add_anti_nodes(antenna_a, antenna_b, anti_nodes_set, matrix):
    """Calculates and adds anti nodes based on alignment of antenna pairs."""
    antenna_ax, antenna_ay = antenna_a
    antenna_bx, antenna_by = antenna_b

    distance_x = antenna_bx - antenna_ax
    distance_y = antenna_by - antenna_ay

    antinode = (antenna_ax - distance_x, antenna_ay - distance_y)

    starting_antinode = get_starting_position(antinode, distance_x, distance_y, matrix)

    if in_bounds(starting_antinode, matrix):
        anti_nodes_set.add(starting_antinode)
        anti_nodes_set = add_all_anti_nodes(starting_antinode, distance_x, distance_y, anti_nodes_set, matrix)

    return anti_nodes_set

def part_two(loc_dict, matrix):
    """Processes all pairs of antennas with the same frequency and calculates the number of anti nodes."""
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
    
    answer = part_two(antenna_locations, puzzle_input)

    print(f'The answer to part two is: {answer}')
    