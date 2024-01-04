import re
# Reads a file, removes specific characters, and returns its content as a 2D list.
def read_file_return_2D_list(file):
     with open(file) as data:
          text_one = re.sub(r'x=|y=|by|s+', '' , data.read())
          text_two = re.sub(r'x', ' ', text_one)

          lines = [line.split() for line in text_two.split('\n') if line.strip()]
     return lines

# Creates a matrix of a given width and height with all elements initialized to a full stop character.
def create_matrix(width, hight):
     matrix = [['.' for _ in range(width)] for _ in range(hight)]
     return matrix

# Turns on pixels (represented by '#') in a matrix up to a specified row and column.
def turn_pixels_on(end_col, end_row, matrix):
     for row in range(end_row):
          for col in range(end_col):
               matrix[row][col] = '#'
     return matrix

# Shifts all elements of a specified row in a matrix by a certain amount.
def shift_row(start_row, shift_amount, matrix):
     for _ in range(shift_amount):
          matrix[start_row] = matrix[start_row][-1:] + matrix[start_row][:-1]
     return matrix

# Gathers elements from a specific column in a matrix.
def get_elements(start_col, matrix):
     elements = []
     
     for i in range(len(matrix)):
          elements.append(matrix[i][start_col])
     return elements

# Shifts all elements of a specified column in a matrix by a certain amount.
def shift_column(start_col, shift_amount, matrix):
     for _ in range(shift_amount):
          pixels = get_elements(start_col, matrix)
          matrix[0][start_col] = pixels[-1]

          for i in range(1, len(matrix)):
               matrix[i][start_col] = pixels[i-1]
     return matrix

# Counts the number of pixels (represented by '#') in a matrix.
def count_pixels(matrix, total=0):
     for row in matrix:
          total += row.count('#')
     return total

# Processes a list of instructions to manipulate the pixels on a screen (matrix).
def part_one(instructions, screen):
     for instruction in instructions:

          if instruction[0] == 'rect':
               start_col = int(instruction[1])
               start_row = int(instruction[2])
               
               screen = turn_pixels_on(int(start_col), int(start_row), screen)
          elif instruction[0] == 'rotate':
               if instruction[1] == 'row':
                    swich_row = int(instruction[2])
                    swich_by = int(instruction[3])

                    screen = shift_row(swich_row, swich_by, screen)
               else: 
                    swich_row = int(instruction[2])
                    swich_by = int(instruction[3])

                    screen = shift_column(swich_row, swich_by, screen)
     return screen

#________Main Program_________ #
if __name__ == "__main__":

     puzzle_input = read_file_return_2D_list('text.txt')

     screen = create_matrix(50, 6)

     adjusted_screen = part_one(puzzle_input, screen)

     answer = count_pixels(adjusted_screen)

     print(f'The answer to part one is: {answer}')