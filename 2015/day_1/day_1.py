'''Day one of advent of code: Solution.'''

# covert the txtfile to a readable string of directions.
def read_file():
    '''This function converts a text file to a string.'''
    with open('text.txt', encoding='utf-8') as file:
        text = file.read()
        return text

# Read the dicrections and returns the floor number and the basement index.
def floor_count(my_string):
    '''This will return the floor number santa must go to and the index of the list that brings santa to the basement.'''

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

    return floor, basement_position

my_instructions = read_file()

floors, basement = floor_count(my_instructions)

print(f'Santans Floor: {floors}\nBasement position: {basement}')
