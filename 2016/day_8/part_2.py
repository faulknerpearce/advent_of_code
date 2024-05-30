from part_1 import read_file_return_2D_list, generate_martix, shift_down, shift_accross, get_pixels_from_column, adjust_pixels

# Outputs every pixel in each row to the terminal.
def print_screen(matrix):
    for row in matrix:
        pixels = ''

        for pixel in row:
            pixels += pixel
        
        print(pixels)

if __name__ == '__main__':

    my_instructions = read_file_return_2D_list('text.txt')

    my_screen = generate_martix(50, 6)

    adjusted_screen = adjust_pixels(my_instructions, my_screen)

    print_screen(adjusted_screen)