def read_file_return_list(file):
    '''Reads a file and returns an array of directions.'''
    with open(file) as data:
        directions = data.read().replace(',', '').split()
    return directions

class Compass:
    '''Compass class to manage orientation and rotations.'''
    def __init__(self):
        self.points = ['N', 'E', 'S', 'W']
        self.current_point = self.points[0]
        
    def rotate(self, direction):
        '''Rotates the compass 90 degrees left ('L') or right ('R') based on the given direction.'''

        increment = -1 if direction == 'L' else 1

        self.current_point = self.points[(self.points.index(self.current_point) + increment) % len(self.points)]
 
def get_distance(instructions, compass):
    '''Calculates the Manhattan distance from the origin based on a set of directions.'''
    x = 0
    y = 0

    for instruction in instructions:
        compass.rotate(instruction[0])

        if compass.current_point == 'N':
            y += int(instruction[1:])

        elif compass.current_point == 'S':
            y -= int(instruction[1:])

        elif compass.current_point == 'E':
            x += int(instruction[1:])
      
        elif compass.current_point == 'W':
            x -= int(instruction[1:])

    return abs(x) + abs(y)

# Event: https://adventofcode.com/2016/day/1
if __name__ == "__main__":

    my_compass = Compass()

    puzzle_input = read_file_return_list('text.txt')

    answer = get_distance(puzzle_input, my_compass)

    print(f'The answer to part one is: {answer}')
