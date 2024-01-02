from  part_1 import read_file_and_return_list

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

#________Main Program_________ # 
if __name__ == "__main__":

    my_input = read_file_and_return_list('text.txt')

    answer = part_two(my_input)

    print(f'Part two: {answer}')