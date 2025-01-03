import re 

def read_file_return_2d_list(file):
    '''Reads the file and returns a 2D list where each sublist contains the dimensions of a box.'''
    with open(file) as text:
        formatted = re.sub(r'x', ' ', text.read())
        instructions = [line.split() for line in formatted.split('\n')]
        
        return instructions
   
def get_slack(l, w, h):
    '''Calculates the slack (smallest side area) of the box.'''
    return min((l * w), (l * h), (w * h))

def calculate_dimensions(instruction):
    '''Calculates the total wrapping paper needed for a single box, including the slack.'''
    length, width, height = int(instruction[0]), int(instruction[1]), int(instruction[2])

    box = (2 * length * width) + (2 * length * height) + (2 * width * height) 
    
    slack = get_slack(length, width, height)
    
    return box + slack

def calculate_total_wrapping_paper(instructions):
    '''Sums up the total wrapping paper needed for all boxes.'''
    total = 0

    for instruction in instructions:
        total += calculate_dimensions(instruction)

    return total

# Event: https://adventofcode.com/2015/day/2
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = calculate_total_wrapping_paper(puzzle_input)

    print(f'The answer to part one is: {answer}')
