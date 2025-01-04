from part_1 import read_file_return_string, move

# Calculate the total houses that santa and the robot visited.
def deliver_presents(instructions):
    visited_houses = set()
    visited_houses.add((0, 0))
    
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0,

    santas_turn = True

    for instruction in instructions:
        if santas_turn:
            santa_x, santa_y = move(santa_x, santa_y, instruction)
            visited_houses.add((santa_x, santa_y))
            santas_turn = False
        
        else:
            robot_x, robot_y = move(robot_x, robot_y, instruction)
            visited_houses.add((robot_x, robot_y))
            santas_turn = True

    return len(visited_houses)

if __name__ == "__main__":

    puzzle_input = read_file_return_string('text.txt')

    answer = deliver_presents(puzzle_input)
    
    print(f'The answer to part two is: {answer}')