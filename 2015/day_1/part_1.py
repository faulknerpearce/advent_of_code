def read_file_return_string(file):
    '''covert the txt file to a readable string of directions.'''
    with open(file) as file:
        text = file.read()
        return text

def floor_count(my_string):
    '''Read the directions and returns the floor number and the basement index.'''
    floor = 0

    for char in my_string:
        if char == "(":
            floor += 1
        else:
            floor -= 1

    return floor

# Event: https://adventofcode.com/2015/day/1 
if __name__ == "__main__":

    puzzle_input = read_file_return_string('text.txt')

    answer = floor_count(puzzle_input)

    print(f'The answer to part one is: {answer}.')
