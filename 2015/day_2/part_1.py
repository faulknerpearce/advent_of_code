import re 

# Reads the file and returns a 2D list where each sublist contains the dimensions of a box.
def read_file_return_2d_list(file):
    with open(file) as text:
        formatted = re.sub(r'x', ' ', text.read())
        instructions = [line.split() for line in formatted.split('\n')]
        
        return instructions

# Calculates the slack (smallest side area) of the box.   
def get_slack(l, w, h):
    return min((l * w), (l * h), (w * h))

# Calculates the total wrapping paper needed for a single box, including the slack.
def calculate_dimensions(instruction):
    length, width, height = int(instruction[0]), int(instruction[1]), int(instruction[2])

    box = (2 * length * width) + (2 * length * height) + (2 * width * height) 
    
    slack = get_slack(length, width, height)
    
    return box + slack

# Sums up the total wrapping paper needed for all boxes.
def calculate_total_wrapping_papper(instructions):
    total = 0

    for instruction in instructions:
        total += calculate_dimensions(instruction)

    return total

if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = calculate_total_wrapping_papper(puzzle_input)

    print(f'The answer to part one is: {answer}')
