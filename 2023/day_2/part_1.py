import re
# Reads a file, formats the content, and creates a list of lines for each game.
def read_file_and_create_list(file):
    with open(file) as data:
        text = data.read()
        formatted = re.sub(r'Game|:|,', '', text)
        lines = formatted.split('\n')
    my_lines = [[word + ';' if i == len(line.split()) - 1 else word for i, word in enumerate(line.split())] for line in lines if line.strip()]
    return my_lines

# Checks if the counts of used colors are within the maximum allowed limits.
def check_valid(used, maximum):
    for key ,value in used.items():
        if value > maximum[key]:  
            return False
    return True

# Checks if rounds are valid based on the counts of colors used.
def check_valid_rounds(line):
    maximum_colours = {'red': 12, 'green': 13, 'blue': 14}
    used_colours = {'red': 0, 'green': 0, 'blue': 0}

    for i in range(1, len(line), 2):
        amount = line[i]
        colour = line[i+1]
        
        # End of round. 
        if ';' in colour:
            used_colours[colour[:-1]] += int(amount)
            
            if check_valid(used_colours, maximum_colours):
                # Reset counts if the round is valid
                used_colours['red'] = 0
                used_colours['green'] = 0
                used_colours['blue'] = 0
            else:
                return False 
        else:
            used_colours[colour] += int(amount)
    return True

# Gets the valid game IDs by checking each round in the lines.
def part_one(lines):
    valid_games = []
    for line in lines:
        game_id = line[0]
        if check_valid_rounds(line):
            valid_games.append(int(game_id))
    return sum(valid_games)

my_input = read_file_and_create_list('text.txt')

answer = part_one(my_input)

print(f'Part one: {answer}')