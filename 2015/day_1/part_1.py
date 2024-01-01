# covert the txtfile to a readable string of directions.
def read_file(file):
    with open(file, encoding='utf-8') as file:
        text = file.read()
        return text

# Read the dicrections and returns the floor number and the basement index.
def floor_count(my_string):
    floor = 0

    for char in my_string:
        if char == "(":
            floor += 1
        else:
            floor -= 1

    return floor

#________Main Program_________ # 
if __name__ == "__main__":
    
    puzzle_input = read_file('text.txt')

    answer = floor_count(puzzle_input)

    print(f'The answer to part ome is: {answer}.')
