from part_1 import read_file_return_string

# This will return the floor number santa must go to and the index of the list that brings santa to the basement..
def basement_position(my_string):
    floor = 0
    position = 0

    for char in my_string:
        position += 1
        
        if char == "(":
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            return position

if __name__ == "__main__":
    
    puzzle_input = read_file_return_string('text.txt')

    answer = basement_position(puzzle_input)

    print(f'The answer to part two is: {answer}.')