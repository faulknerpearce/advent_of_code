from part_1 import read_file_return_3d_array, create_rules_map, check_printing_order

# Fixes the printing order of an array based on dependency rules in the map.
def fix_printing_order(array, map):
    ordered = []  
    unordered = set(array)

    while unordered:

        for num in list(unordered):
            valid = True
            
            for dep in map.get(num, []):  
                if dep in unordered: 
                    valid = False
                    break

            if valid:  
                ordered.append(num)  
                unordered.remove(num)  

    return ordered

# Processes updates and fixes their order if they are invalid.
def get_fixed_updates(arrays, map):
    valid_updates = []

    for array in arrays:
        if not check_printing_order(array, map):
            reordered_array = fix_printing_order(array, map)
            valid_updates.append(reordered_array)
    
    return valid_updates

# Computes the sum of the middle values of fixed invalid updates.
def part_two(updates, rules_map):
    total = 0

    valid_fixed_updates = get_fixed_updates(updates, rules_map)

    for update in valid_fixed_updates:
        total += update[len(update) //2]

    return total 

 # Event: https://adventofcode.com/2024/day/5
if __name__ == '__main__':
    
    puzzle_input = read_file_return_3d_array('text.txt') 

    ordering_rules = create_rules_map(puzzle_input[0])

    answer = part_two(puzzle_input[1], ordering_rules)

    print(f'The answer to part two is: {answer}')
