
# covert the txtfile to a readable string of directions.
def read_file():
    with open('text.txt', encoding='utf-8') as file:
        text = file.read()
        return text

# This will return the floor number santa must go to and the index of the list that brings santa to the basement..
def basement_position(my_string):
    floor = 0
    position = 0
    breaker = 0

    for char in my_string:
        if char == "(":
            floor += 1
            position += 1
        else:
            floor -= 1
            position += 1

        if floor == -1 and breaker != 1:
            basement_position = position
            breaker += 1
            break

    return basement_position

# ________Main Program_________ #
my_input = read_file()

basement = basement_position(my_input)

print(f'The answer to part two is: {basement}.')