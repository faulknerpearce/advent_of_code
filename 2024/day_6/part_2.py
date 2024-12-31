class Guard:
    '''Guard initialized with position, direction, and visited states.'''
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.visited_states = set()  # Tracks (row, col, direction)

    def traverse(self, matrix):
        '''Simulates movement and checks for loops.'''
        # Directions: ^ > v <
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir_idx = self.direction

        while True:
            # Track the current state
            state = (self.row, self.col, dir_idx)

            # Loop detected if the same state is revisited
            if state in self.visited_states:
                return True  # LOOP DETECTED

            # Mark the state as visited
            self.visited_states.add(state)

            # Move forward
            dr, dc = directions[dir_idx]
            next_row, next_col = self.row + dr, self.col + dc

            # Check bounds
            if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
                return False  # EXIT GRID (no loop)

            # Obstruction
            if matrix[next_row][next_col] == '#':
                # Turn right
                dir_idx = (dir_idx + 1) % 4
            else:
                # Move forward
                self.row, self.col = next_row, next_col

def read_file_return_2d_list(file):
    '''Reads a file and returns the content as a 2D array.'''
    with open(file) as data:
        array = [list(line.strip('\n')) for line in data.readlines()]
    return array


def get_starting_position_and_direction(matrix):
    '''Find the starting position and initial direction of the guard.'''
    directions = {'^': 0, '>': 1, 'v': 2, '<': 3}  # Map symbols to direction indices

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] in directions:
                return row, col, directions[matrix[row][col]]


def simulate_with_obstruction(matrix, row, col):
    '''Simulates the guard with a temporary obstruction.'''
    # Place obstruction
    matrix[row][col] = '#'

    # Find guard's initial position and direction
    start_row, start_col, direction = get_starting_position_and_direction(matrix)

    # Simulate with the obstruction
    guard = Guard(start_row, start_col, direction)
    result = guard.traverse(matrix)  # True if loop detected

    # Remove the obstruction
    matrix[row][col] = '.'

    return result

def part_two(matrix):
    '''Counts positions where placing an obstruction creates a loop.'''
    loop_positions = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '.':
                start_row, start_col, _ = get_starting_position_and_direction(matrix)

                if (row, col) == (start_row, start_col):
                    continue

                if simulate_with_obstruction(matrix, row, col):
                    loop_positions += 1

    return loop_positions

# Event: https://adventofcode.com/2024/day/6
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')
