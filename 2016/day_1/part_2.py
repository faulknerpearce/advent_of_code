from part_1 import Compass, read_file_return_list

# Processes directions to find the first location visited twice and returns its Manhattan distance from the origin
def part_two(directions, compass):
    x = 0 
    y = 0
    visited = set()
    visited.add((x, y))

    for direction in directions:
        compass.rotate(direction[0])
        steps = int(direction[1:])
        
        for _ in range(steps):
            if compass.current_point == 'N':
                y += 1
            elif compass.current_point == 'S':
                y -= 1
            elif compass.current_point == 'E':
                x += 1
            elif compass.current_point == 'W':
                x -= 1

            if (x, y) in visited:
                return abs(x) + abs(y)
           
            visited.add((x, y))

#________Main Program_________ # 
if __name__ == "__main__":

    my_compass = Compass()

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input, my_compass) 

    print(f'The answer to part two is: {answer}')