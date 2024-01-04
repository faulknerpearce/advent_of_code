from part_1 import read_file_return_2D_list, create_matrix, turn_pixels_on, shift_row, shift_column, get_elements

# Prints the elements of a matrix, formatting them as a grid.
def print_screen(matrix):
     string = ''
     for i in range(len(matrix)):
          for j in range(len(matrix[i])):
               string += matrix[i][j]
          print(string)
          string = ''

# Processes a list of instructions to manipulate the pixels on a screen (matrix).
def part_two(instructions, screen):
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

    adjusted_screen = part_two(puzzle_input, screen)

    print_screen(adjusted_screen)
