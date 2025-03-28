# Reads a file and returns an array of directions.
def read_file_return_list(file):
    with open(file) as data:
        directions = data.read().replace(',', '').split()
    return directions

# Defines a Compass class to manage orientation and rotations
class Compass:
    def __init__(self):
        self.points = ['N', 'E', 'S', 'W']
        self.current_point = self.points[0]
        
    # Returns the current position of the compass 
    def rotate(self, direction):
        if direction == 'R':
            direction_num = +1
        else:
            direction_num = -1
        
        new_index = (self.points.index(self.current_point) + direction_num) % len(self.points)
        self.current_point = self.points[new_index]

# Calculates the Manhattan distance from the origin based on a set of directions  
def get_distance(instructions, compass):
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

#________Main Program_________ # 
if __name__ == "__main__":

    my_compass = Compass()

    puzzle_input = read_file_return_list('text.txt')

    answer = get_distance(puzzle_input, my_compass)

    print(f'The answer to part one is: {answer}')
