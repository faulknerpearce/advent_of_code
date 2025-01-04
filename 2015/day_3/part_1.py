# Read from a text file and return the data as a string.
def read_file_return_string(file):
    with open(file, encoding="utf-8") as file:
        text = file.read()
    return text

# Moves the current position based on the given instruction.
def move(x, y, instruction):

    if instruction == '^':
        x += 1
    elif instruction == 'v':
        x -= 1
    elif instruction == '>':
        y += 1
    else:
        y -= 1

    return x, y  

# Calculate the total houses that santa visited.
def deliver_presents(instructions):
    visited_houses = set()
    visited_houses.add((0, 0))
    x, y = 0, 0

    for instruction in instructions :

        x, y = move(x, y, instruction)
        
        visited_houses.add((x, y))

    return len(visited_houses)

if __name__ == "__main__":

    puzzle_input = read_file_return_string('text.txt')

    answer = deliver_presents(puzzle_input)
    
    print(f'The answer to part one is: {answer}')