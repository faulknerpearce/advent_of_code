from part_1 import read_file

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

#________Main Program_________ # 
if __name__ == "__main__":
    
    my_input = read_file('text.txt')

    answer = basement_position(my_input)

    print(f'The answer to part two is: {answer}.')