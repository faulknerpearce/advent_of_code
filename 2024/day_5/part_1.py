import re 

# Reads a file and converts its content into a 3D array of integers for ordering rules and updates.
def read_file_return_3d_array(file):
    with open(file) as data:
     
        ordering_rules, updates = data.read().strip().split("\n\n")
        
        ordering_rules_array = [[int(num) for num in line.split('|')] for line in ordering_rules.splitlines()]
        updates_array = [[int(num) for num in line.split(',')] for line in updates.splitlines()]
        
        return [ordering_rules_array, updates_array]
    
# Creates a mapping of rules where each key maps to a list of its associated values that come after it.
def create_rules_map(rules):
    rules_map = {}

    for rule in rules:
        
        if rules_map.get(rule[0]):
            rules_map[rule[0]].append(rule[1])
        else:
            rules_map.update({rule[0]: [rule[1]]})
    
    return rules_map

# Validates if pages follow the correct order based on printing rules for ascending or descending constraints.
def valid_order(key, array, past_numbers, map, ascending):
    if ascending:
        for number in array:
            if number not in map[key]:
                return False
    else:
        for number in past_numbers:
            if number in map[key]:
                return False
             
    return True

# Checks if the printing order of an array follows the ordering rules in the given map.
def check_printing_order(array, map):
    past_numbers = []

    for i in range(len(array)):

        if map.get(array[i]):
            
            if not valid_order(array[i], array[i+1:],past_numbers,  map, True) or not valid_order(array[i], array[i+1:],past_numbers,  map, False) :
                return False
        
        past_numbers.append(array[i])

    return True

# Filters and returns only the updates that follow the printing order rules.
def get_valid_updates(arrays, map):
    valid_updates = []

    for array in arrays:
        if check_printing_order(array, map):
            valid_updates.append(array)
    
    return valid_updates

# Calculates the total sum of the middle values from valid updates.
def part_one(updates, rules_map):
    total = 0

    valid_updates = get_valid_updates(updates, rules_map)

    for update in valid_updates:
        total += update[len(update) //2]

    return total 

 # Event: https://adventofcode.com/2024/day/5
if __name__ == '__main__':

    puzzle_input = read_file_return_3d_array('text.txt')

    ordering_rules_map = create_rules_map(puzzle_input[0])

    answer = part_one(puzzle_input[1], ordering_rules_map)

    print(f'The answer to part one is: {answer}')
