import re
# Reads a file, formats the content, and creates a list of lines for each game.
def read_file_and_create_list(file):
    with open(file) as data:
        text = data.read()
        formatted = re.sub(r'Game|:|,', '', text)
        lines = formatted.split('\n')
    my_lines = [[word + ';' if i == len(line.split()) - 1 else word for i, word in enumerate(line.split())] for line in lines if line.strip()]
    return my_lines

# Checks if rounds are valid based on the counts of colors used.
def get_minimum(line):
    used_colours = {'red': 0, 'green': 0, 'blue': 0}
    for i in range(1, len(line), 2):
        amount = int(line[i])
        colour = line[i+1]
        
        if ';' in colour:
            if amount > used_colours[colour[:-1]]:
                used_colours[colour[:-1]] = int(amount)
        else:
            if amount > used_colours[colour]:
                used_colours[colour] = int(amount)
    return used_colours

# Multiply all minimum red, green, and blue values per line into variable called "product"
def get_product(min_colours):
    red = min_colours['red']
    green = min_colours['green']
    blue = min_colours['blue']
    
    product = red * green * blue
    return product

def part_two(lines):
    products = []
    for line in lines:
        my_colours = get_minimum(line)
        my_product = get_product(my_colours)
        products.append(my_product)

    return sum(products)

my_input = read_file_and_create_list('text.txt')

answer = part_two(my_input)

print(f'Part two: {answer}')