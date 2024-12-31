class Robot:
    '''Guard class initialized with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def attempt_vertical_push(self, row_step, matrix):
        '''Attempts to push a box in the specified direction; up, down.'''
        first_box_index = None
        
        for i in range(self.row + row_step, self.row + (row_step * len(matrix)), row_step):
            if matrix[i][self.col] == 'O' and first_box_index is None:
                first_box_index = i
            
            elif matrix[i][self.col] == '.' and first_box_index is not None:
                # Move the box to the empty position.
                matrix[i][self.col] = 'O'
                matrix[first_box_index][self.col] = '.'
                
                # Move the robot to the box's previous position.
                matrix[first_box_index][self.col] = '@'
                matrix[self.row][self.col] = '.'

                # Update robot's position to the box's old position.
                self.row = first_box_index
                break
            
            elif matrix[i][self.col] == '#':
                break
      
        return matrix
    
    def attempt_horizontal_push(self, col_step, matrix):
        '''Attempts to push a box in the specified direction; left or right.'''
        first_box_index = None

        for i in range(self.col + col_step, self.col + (col_step * len(matrix)), col_step):
            if matrix[self.row][i] == 'O' and first_box_index is None:
                first_box_index = i
            
            elif matrix[self.row][i] == '.'and first_box_index is not None:
                # Move the box to the empty position.
                matrix[self.row][i] = 'O'
                matrix[self.row][first_box_index] = '.'
                
                # Move the robot to the box's previous position.
                matrix[self.row][first_box_index] = '@'
                matrix[self.row][self.col] = '.'

                # Update robot's position to the box's old position.
                self.col = first_box_index
                break

            elif matrix[self.row][i] == '#':
                break

        return matrix
       
    def attempt_move(self, row, row_step, col, col_step, matrix):
        '''Attempts to move the robot to a new position based on direction, pushing boxes if necessary.'''
        # If a box was found attempt to push it.
        if matrix[row][col] == 'O':

            if col_step == 0:
                matrix = self.attempt_vertical_push(row_step, matrix)
            else:
                matrix = self.attempt_horizontal_push(col_step, matrix)

            return matrix
        # If a free space is found move the robot to the new position.
        elif matrix[row][col] == '.':
            matrix[self.row][self.col], matrix[row][col] = matrix[row][col], matrix[self.row][self.col]
            self.row = row 
            self.col = col 
            
            return matrix
        # If no box or space is found do nothing.
        else:
            return matrix

    def move(self, row_step, col_step, matrix):
        '''Moves the robot in the given direction, row or column, based on instructions provided.'''
        # Row traversal.
        if col_step == 0:
            matrix = self.attempt_move(self.row + row_step, row_step, self.col, col_step, matrix)
        # Column traversal.
        else:
            matrix = self.attempt_move(self.row, row_step, self.col + col_step, col_step, matrix)

        return matrix  
                
def read_file_return_split_lists(file):
    '''Reads the input file and splits it into the warehouse matrix and movement instructions.'''
    with open(file) as data:

        text = data.read().split('\n\n')
        map = [list(row) for row in text[0].split('\n')]
        directions = text[1].replace('\n', '')

    return map, directions

def get_starting_position(matrix):
    '''Finds the initial position of the robot (x, y) in the matrix.'''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '@':
                return row, col

def calculate_distance(item, matrix):
    '''Calculates the total weighted distance of all boxes based on their positions.'''
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] == item:
                total += 100 * i + j
    return total

def part_one(robot, instructions, matrix):
    '''Executes all movement instructions, updates the matrix, and calculates the final result.'''
    move_dict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}

    for instruction in instructions:
     
        x, y = move_dict.get(instruction)
        matrix = robot.move(x, y, matrix)

    return calculate_distance('O', matrix)

# Event: https://adventofcode.com/2024/day/15 
if __name__ == '__main__':

    warehouse, directions = read_file_return_split_lists('text.txt')

    starting_row, starting_col = get_starting_position(warehouse)

    warehouse_robot = Robot(starting_row, starting_col)

    answer = part_one(warehouse_robot, directions, warehouse)

    print(f'The answer to part one is: {answer}')
