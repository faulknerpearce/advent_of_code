def read_file_return_list(file):
    with open(file) as data:
        directions = data.read().replace(',', '').split()
    return directions

class Compass:
    def __init__(self, current_position='N'):
        self.current_position = current_position
        self.points = ['N', 'E', 'S', 'W']
        
    def rotate(self, direction):
        index = self.points.index(self.current_position)
        if direction == 'R':
            self.current_position = self.points[(index + 1) % len(self.points)]
        else:
            self.current_position = self.points[(index - 1) % len(self.points)]

    def get_position(self):
        return self.current_position
    
    def get_behind(self):
        index = self.points.index(self.current_position)
        behind = self.points[(index + 2) % len(self.points)]
        return behind
 
def walk_blocks(directions, compass):
    blocks_walked = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    for direction in directions:
        compass.rotate(direction[0])
        behind = compass.get_behind()
        infrount = compass.get_position()

        if blocks_walked[behind] > 0:
            blocks_walked[behind] -= int(direction[1])
        else:
            blocks_walked[infrount] += int(direction[1])

    return blocks_walked

def get_distance(blocks_walked):
    latitude = abs(blocks_walked['E'] - blocks_walked['W'])
    longitude = abs(blocks_walked['N'] - blocks_walked['S'])

    blocks_away = latitude + longitude

    return blocks_away

# ________Main Program_________ # 
my_compass = Compass()

my_input = read_file_return_list('text.txt')

moves = walk_blocks(my_input, my_compass)

distance_walked = get_distance(moves)

print(f'The answer to part one is: {distance_walked}. \nMoves: {moves}')
