# Day 3 Part 1 
visited_houses = set()
visited_houses.add((0, 0)) # Santa starts by delivering a present at his starting location

def get_directions():
    with open("text.txt") as file:
        text = file.read()
    return text

def walk_to(direction, houses):
    x, y = 0, 0  # Starting coordinates
    for step in direction:
        if step == "^":
            y += 1
        elif step == "v":
            y -= 1
        elif step == ">":
            x += 1
        elif step == "<":
            x -= 1
        # After each step, add the house to the visited_houses set if, it is a new number
        houses.add((x, y))
        
    return len(houses)

directions = get_directions()

print(walk_to(directions, visited_houses))
