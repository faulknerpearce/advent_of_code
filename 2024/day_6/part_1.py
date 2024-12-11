class Guard:
    # Initialize Guard with starting position.
    def __init__(self, row, col):
        self.distinct_positions = set() 
        self.row = row
        self.col = col
    
     # Traverse through rows, moving up or down
    def traverse_row(self, array, move_up):
        for i in range(1, len(array)):

            if move_up:
                if self.row-i == -1:
                    return True
        
                elif array[self.row-i][self.col] == '#':
                    self.row = (self.row - (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row-i, self.col))
                    
            else:
                if self.row+i == len(array):
                    return True
            
                elif array[self.row+i][self.col] == '#':
                    self.row = (self.row + (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row+i, self.col))

    # Traverse through columns, moving left or right
    def traverse_col(self, array, move_left):
        for i in range(1, len(array)):

            if move_left:
                if self.col-i == -1:
                    return True
            
                elif array[self.row][self.col-i] == '#':
                    self.col = (self.col - (i-1))
                    return False 
                else:
                    self.distinct_positions.add((self.row, self.col-i))

            else:
                if self.col+i == len(array):
                    return True
                
                elif array[self.row][self.col+i] == '#':
                    self.col = (self.col + (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row, self.col+i))

# Reads a file and returns the content as a 2D array.
def read_file_return_2d_list(file):
    with open(file) as data:

        array = [line.strip('\n') for line in data.readlines()]

    return array

# Find starting position (x, y) marked by '^'                
def get_starting_position(arrays):
    for row in range(len(arrays)):
        for col in range(len(arrays[row])):
            if arrays[row][col] == '^':
               return row, col

# Traverse map in a cyclic pattern until edge reached.            
def part_one(guard, array):
    direction = 1
    end_of_map = False

    while not end_of_map:

        if direction == 1:
            end_of_map = guard.traverse_row(array, True)
            direction += 1
            
        elif direction == 2:
            end_of_map = guard.traverse_col(array, False)
            direction += 1


        elif direction == 3:
            end_of_map = guard.traverse_row(array, False)
            direction += 1

        else:
            end_of_map = guard.traverse_col(array, True)
            direction = 1

    return len(guard.distinct_positions)
 
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    x, y = get_starting_position(puzzle_input)

    my_guard = Guard(x, y)

    my_guard.distinct_positions.add((x, y))

    answer = part_one(my_guard, puzzle_input)

    print(f'The answer to part one is: {answer}')
