from part_1 import read_file_return_split_lists, get_starting_position, calculate_distance

class Robot:
    '''Guard class initialized with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def verify_and_attempt_vertical_push(self, row_step, box_dict, matrix, verify_only=False):
        '''Moves boxes vertically based on the specified step direction, verifying space if required.'''
        
        keys = sorted(box_dict, reverse=(row_step == 1)) # Sort keys based on row_step direction

        new_matrix = matrix if not verify_only else None

        for key in keys: # Unpacks the keys (rows) of the consecutive boxes.
            for i in box_dict[key]:
                
                if key + row_step < 0 or key + row_step >= len(matrix): # Check if the target row is within bounds.
                    return False if verify_only else matrix

                
                if matrix[key + row_step][i] in ['.', '[', ']']: # Check if the target position is free.
                    if not verify_only: 
                        new_matrix[key + row_step][i] = matrix[key][i]
                        new_matrix[key][i] = '.'
               
                elif matrix[key + row_step][i] == '#':
                    return False if verify_only else matrix

        if not verify_only: # Update the robot's position only if pushing boxes
            self.row += row_step
            return new_matrix

        return True
    
    def attempt_horizontal_push(self, col_step, matrix):
        '''Attempts to push a box horizontally in the given direction ( left or right ).'''
        first_side_index = None
        
        for i in range(self.col + col_step, self.col + (col_step * len(matrix)), col_step):

            if (matrix[self.row][i] == '[' or matrix[self.row][i] == ']') and first_side_index is None:
                first_side_index = i
            
            elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == 1: # Identify first box side traversing left to right.
                
                matrix[self.row] = matrix[self.row][:self.col] + list('.') + matrix[self.row][self.col:i] + matrix[self.row][i + 1:] # Slice to the left.
                
                self.col = first_side_index
                break
            
            elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == -1: # Identify first box side traversing right to left.
                
                matrix[self.row] = matrix[self.row][:i] + matrix[self.row][i + 1:first_side_index + 2] + list('.') + matrix[self.row][self.col + 1:] # Slice to the right.
                
                self.col = first_side_index
                break
            
            elif matrix[self.row][i] == '#':
                break

        return matrix
                
    def attempt_move(self, row, row_step, col, col_step, matrix):
        '''Attempts to push a box in the specified direction; up, down, left or right.'''
        
        if matrix[row][col] == '[' or matrix[row][col] == ']': # Check if target cell has a box.
            
            if col_step == 0: # Handle vertical movement.
                box_positions = find_consecutive_boxes(self.row, self.col, row_step, matrix)

                space = self.verify_and_attempt_vertical_push(row_step, box_positions, matrix, verify_only=True)
                
                if space: # Move boxes if space is available.
                    matrix = self.verify_and_attempt_vertical_push(row_step, box_positions, matrix, verify_only=False)

            else: # Handle horizontal movement.
                matrix = self.attempt_horizontal_push(col_step, matrix)
                
            return matrix
        
        elif matrix[row][col] == '.': # Move the robot if the target cell is empty.
            matrix[self.row][self.col], matrix[row][col] = matrix[row][col], matrix[self.row][self.col]
            self.row = row 
            self.col = col
            
            return matrix
        
        else: # Return unchanged matrix if movement is invalid.
            return matrix

    def move(self, row_step, col_step, matrix):
        '''Moves the robot in the given direction, row or column, based on instructions provided.'''
       
        if col_step == 0: # Handle vertical movement.
            matrix = self.attempt_move(self.row+row_step, row_step, self.col, col_step, matrix)
        
        else: # Handle horizontal movement.
            matrix = self.attempt_move(self.row, row_step, self.col+col_step, col_step, matrix)

        return matrix
    
def find_consecutive_boxes(pos_row, pos_col, row_step, matrix):
    '''Finds and groups consecutive boxes along a vertical path.'''
    box_positions = {pos_row: [pos_col]} 
    last_key = pos_row

    for row in range(pos_row+ row_step, pos_row + (row_step * len(matrix)), row_step):
        boxes = []
       
        if row < 0 or row >= len(matrix): # Stop at boundaries.
            break
        
        for i in range(len(matrix[row])): # Detect consecutive boxes and track their positions.
            if matrix[row][i] == '[':
                if i in box_positions[last_key] or i + 1 in box_positions[last_key]:
                    boxes.extend([i, i +1])
        if boxes: # If boxes were found add them to the dictionary.
            box_positions[row] = boxes
            last_key = row 
        else:
            return box_positions           
        
    return box_positions

def transform(matrix):
    '''Transforms input matrix symbols into an expanded version.'''
    new_matrix = []

    for row in matrix:
        line = ''
        
        for col in row:
            if col == "#":
                line += '##'
            elif col == '.':
                line += '..'    
            elif col == 'O':
                line += '[]'
            else:
                line += '@.'
        
        new_matrix.append(list(line))
        
    return new_matrix

def part_two(robot, instructions, matrix):
    '''Executes all movement instructions, updates the matrix, and calculates the final result.'''
    move_dict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}

    for instruction in instructions:

        x, y = move_dict.get(instruction)
        matrix = robot.move(x, y, matrix)

    return calculate_distance('[', matrix)

# Event: https://adventofcode.com/2024/day/15 
if __name__ == '__main__':

    warehouse, directions = read_file_return_split_lists('text.txt')

    large_warehouse = transform(warehouse)

    starting_row, starting_col = get_starting_position(large_warehouse)

    warehouse_robot = Robot(starting_row, starting_col)

    answer = part_two(warehouse_robot, directions, large_warehouse)

    print(f'The answer to part one is: {answer}')