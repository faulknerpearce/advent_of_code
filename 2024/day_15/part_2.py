from part_1 import read_file_return_split_lists, get_starting_position, calculate_distance

class Robot:
    '''Guard class initialized with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def find_consecutive_boxes(self, row_step, matrix):
            box_positions = {self.row: [self.col]} 
            last_key = self.row
       
            for row in range(self.row + row_step, self.row + (row_step * len(matrix)), row_step):
                boxes = []

                # Ensure that the row is not out of bounds.
                if row < 0 or row >= len(matrix):
                    break
                
                # Traverse the column adding any boxes that are connected.
                for i in range(len(matrix[row])):
                    if matrix[row][i] == '[':
                        if i in box_positions[last_key] or i + 1 in box_positions[last_key]:
                            boxes.extend([i, i +1])
                if boxes:
                    box_positions[row] = boxes
                    last_key = row 
                else:
                    return box_positions           
                
            return box_positions
    
    def verify_and_push_boxes(self, row_step, box_dict, matrix, verify_only=False):
        # Sort keys based on row_step direction
        keys = sorted(box_dict, reverse=(row_step == 1))

        # Copy the matrix for modification
        new_matrix = matrix if not verify_only else None

        for key in keys:
            for i in box_dict[key]:
                # Check if the target row is valid
                target_row = key + row_step
                if target_row < 0 or target_row >= len(matrix):
                    return False if verify_only else matrix

                # Check if the target position is free or can accommodate a box
                if matrix[target_row][i] in ['.', '[', ']']:
                    if not verify_only:  # Move the box
                        new_matrix[target_row][i] = matrix[key][i]
                        new_matrix[key][i] = '.'
                # Stop if there's an obstacle
                elif matrix[target_row][i] == '#':
                    return False if verify_only else matrix

        # Update the robot's position only if pushing boxes
        if not verify_only:
            self.row += row_step
            return new_matrix

        return True
    
    def attempt_horizontal_push(self, col_step, matrix):
            first_side_index = None
            
            for i in range(self.col + col_step, self.col + (col_step * len(matrix)), col_step):
                
                if (matrix[self.row][i] == '[' or matrix[self.row][i] == ']') and first_side_index is None:
                    first_side_index = i
                
                elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == 1:
                    # Slice The column across to the right.
                    matrix[self.row] = matrix[self.row][:self.col] + list('.') + matrix[self.row][self.col:i] + matrix[self.row][i + 1:]
                    # Update robot's position to the box's old position.
                    self.col = first_side_index
                    break
                
                elif matrix[self.row][i] == '.' and first_side_index is not None and col_step == -1:
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
                box_positions = self.find_consecutive_boxes(row_step, matrix)

                space = self.verify_and_push_boxes(row_step, box_positions, matrix, verify_only=True)

                if space:
                    matrix = self.verify_and_push_boxes(row_step, box_positions, matrix, verify_only=False)

            else:
                matrix = self.attempt_horizontal_push(col_step, matrix)
                
            return matrix

        elif matrix[row][col] == '.':
            matrix[self.row][self.col], matrix[row][col] = matrix[row][col], matrix[self.row][self.col]
            self.row = row 
            self.col = col
            
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

def part_two(robot, instructions, matrix):
    move_dict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}

    for instruction in instructions:

        x, y = move_dict.get(instruction)
        matrix = robot.move(x, y, matrix)

    return calculate_distance('[', matrix)

if __name__ == '__main__':

    warehouse, directions = read_file_return_split_lists('text.txt')

    large_warehouse = transform(warehouse)

    starting_row, starting_col = get_starting_position(large_warehouse)

    warehouse_robot = Robot(starting_row, starting_col)

    answer = part_two(warehouse_robot, directions, large_warehouse)

    print(f'The answer to part one is: {answer}')