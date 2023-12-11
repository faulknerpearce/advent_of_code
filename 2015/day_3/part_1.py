# This will read from a text file and retrun the data as a string.
def read_file_return_string(file):
    with open(file, encoding="utf-8") as file:
        text = file.read()
    return text

# This will calculate the total steps of santa and the robot.
def deliver_presents_with_robot(directions):
    x, y = 0, 0
    visited_houses = set()
    visited_houses.add((0, 0))

    for direction in directions :

        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1

        visited_houses.add((x, y))

    return len(visited_houses)

# ________Main Program_________ #
my_input = read_file_return_string('text.txt')

answer = deliver_presents_with_robot(my_input)
print(f'The answer to part one is: {answer}')