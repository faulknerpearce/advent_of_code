from part_1 import Compass, read_file_return_list

# Processes directions to find the first location visited twice and returns its Manhattan distance from the origin
def part_two(directions, compass, x=0, y=0):
    seen = set()
    seen.add((x, y))

    for direction in directions:
        compass.rotate(direction[0])
        position = compass.return_position()
        steps = int(direction[1:])
        
        for _ in range(steps):
            if position == 'N':
                y += 1
            elif position == 'S':
                y -= 1
            elif position == 'E':
                x += 1
            elif position == 'W':
                x -= 1

            if (x, y) in seen:
                return abs(x) + abs(y)
           
            seen.add((x, y))
            print(seen)

#________Main Program_________ # 
if __name__ == "__main__":

    my_compass = Compass()

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input, my_compass) 

    print(f'The answer to part two is: {answer}')