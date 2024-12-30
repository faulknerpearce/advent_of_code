from part_1 import read_file_return_split_lists, get_starting_position, calculate_distance
import time, os

class Robot:
    '''Guard class initialized with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def attempt_box_push_row(self, row_step, matrix):
            first_side_index = None
            
            for i in range(self.row+row_step, self.row+(row_step * len(matrix)), row_step):

                if (matrix[i][self.col] == '[' or matrix[i][self.col] == ']') and first_side_index is None:
                    first_side_index = i
                
                elif matrix[i][self.col] == '.' and first_side_index is not None:
                    # Slice The Box to the empty position.
                    
                    # Slice the robot to the box's previous position.
          
                    # Update robot's position to the box's old position.
                    break
                 
                elif matrix[i][self.col] == '#':
                    break

            return matrix
    
    def attempt_box_push_col(self, col_step, matrix):
            first_side_index = None
            
            for i in range(self.col+col_step, self.col+(col_step * len(matrix)), col_step):
                
                if (matrix[self.row][i] == '[' or matrix[self.row][i] == ']') and first_side_index is None:
                    first_side_index = i
                
                elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == 1: # Slice to the right
                    # Slice The column across to the right.
                    matrix[self.row] = matrix[self.row][:self.col] + list('.') + matrix[self.row][self.col:i] + matrix[self.row][i + 1:]
                
                    # Update robot's position to the box's old position.
                    self.col = first_side_index
                    break
                
                elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == -1: # Slice to the left
                    # Slice The column across to the left.
                    matrix[self.row] = matrix[self.row][:i] + matrix[self.row][i + 1:first_side_index + 2] + list('.') + matrix[self.row][self.col + 1:]
                    # Update robot's position to the box's old position.
                    self.col = first_side_index
                    break

                elif matrix[self.row][i] == '#':
                    break

            return matrix
                
    def attempt_move(self, row, row_step, col, col_step, matrix):
   
        if matrix[row][col] == '[' or matrix[row][col] == ']':

            if col_step == 0:
                matrix = self.attempt_box_push_row(row_step, matrix)
            
            else:
                matrix = self.attempt_box_push_col(col_step, matrix)
                
            return matrix

        elif matrix[row][col] == '.':
            matrix[self.row][self.col], matrix[row][col] = matrix[row][col], matrix[self.row][self.col]
            self.row = row # update the robots current row 
            self.col = col # update the robots current col
            
            return matrix
    
        else:
            return matrix

    def move(self, row_step, col_step, matrix):
        # Row traversal.
        if col_step == 0:
            matrix = self.attempt_move(self.row+row_step, row_step, self.col, col_step, matrix)

        # Column traversal.
        else:
            matrix = self.attempt_move(self.row, row_step, self.col+col_step, col_step, matrix)

        return matrix

def transform(matrix):
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

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def animate_matrix(matrix, delay=0.4):
    """Displays the matrix in a loop to simulate animation."""
    os.system('clear')
    for row in matrix:
        print(''.join(row))
    time.sleep(delay)

def part_two(robot, instructions, matrix):
    move_dict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}

    for instruction in instructions:

        print('Before push')
        print(print_matrix(matrix))
     
        x, y = move_dict.get(instruction)
        matrix = robot.move(x, y, matrix)

        print('After push')
        print(print_matrix(matrix))

    return calculate_distance('[', matrix)

if __name__ == '__main__':

    warehouse, directions = read_file_return_split_lists('test_2.txt')

    # large_warehouse = transform(warehouse)

    # starting_row, starting_col = get_starting_position(large_warehouse)

    # warehouse_robot = Robot(starting_row, starting_col)

    # answer = part_two(warehouse_robot, '<', large_warehouse)

    starting_row, starting_col = get_starting_position(warehouse)

    warehouse_robot = Robot(starting_row, starting_col)

    answer = part_two(warehouse_robot, '<<', warehouse)