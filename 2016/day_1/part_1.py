# Reads a file and returns an array of directions.
def read_file_return_list(file):
    with open(file) as data:
        directions = data.read().replace(',', '').split()
    return directions

# Defines a Compass class to manage orientation and rotations
class Compass:
    def __init__(self, current_position='N'):
        self.current_position = current_position
        self.points = ['N', 'E', 'S', 'W']

    # Returns the current position of the compass 
    def rotate(self, direction):
        index = self.points.index(self.current_position)
        if direction == 'R':
            self.current_position = self.points[(index + 1) % len(self.points)]
        else:
            self.current_position = self.points[(index - 1) % len(self.points)]

    # Returns the current position of the compass    
    def return_position(self):
        return self.current_position

# Calculates the Manhattan distance from the origin based on a set of directions  
def part_one(directions, compass, x=0, y=0):

    for direction in directions:
        compass.rotate(direction[0])
        position = compass.return_position()
       
        if position == 'N':
            y += int(direction[1:])
        elif position == 'S':
            y -= int(direction[1:])
        elif position == 'E':
            x += int(direction[1:])
        elif position == 'W':
            x -= int(direction[1:])
    
    return abs(x) + abs(y)
 
#________Main Program_________ # 
if __name__ == "__main__":

    my_compass = Compass()

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input, my_compass)

    print(f'The answer to part one is: {answer}')