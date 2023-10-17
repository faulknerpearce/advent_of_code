def get_directions():
    with open("text.txt") as file:
        text = file.read()
    return text

def deliver_presents_with_robot(directions, robot=True):
    santa_x, santa_y, robo_x, robo_y = 0, 0, 0, 0
    visited_houses = set()
    visited_houses.add((0, 0))

    for i, direction in enumerate(directions):
        if robot and i % 2 != 0:
            # Robo-Santa's turn (if robot is True and it's an odd step)
            x, y = robo_x, robo_y
        else:
            # Santa's turn (if robot is False or it's an even step)
            x, y = santa_x, santa_y

        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1

        visited_houses.add((x, y))

        if robot and i % 2 != 0:
            robo_x, robo_y = x, y
        else:
            santa_x, santa_y = x, y

    return len(visited_houses)

directions = get_directions()

result = deliver_presents_with_robot(directions)
print("Result:", result)
