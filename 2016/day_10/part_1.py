import re 

# Reads a file, applies regex substitutions, and returns a list of processed instructions
def read_file_return_2D_list(file):
    with open(file) as data:
      
        strings = re.sub(r'goes|to|gives|and|bot', '', data.read())

        instructions = [re.sub(r'(output)\s+(\w+)', r'\1_\2', line).split() for line in strings.split('\n') if line.strip()]

    return instructions

# Extracts initial microchip distributions to robots from the set of instructions
def get_microchips_from_input_bins(instructions):
    remaining_instructions = []
    robots = {}

    for instruction in instructions:

        if instruction[0] == 'value':

            if robots.get(instruction[2]):
                robots[instruction[2]].append(instruction[1])
            else:
                robots.update({instruction[2]: [instruction[1]]})
        else: 
            remaining_instructions.append(instruction)
        
    return robots, remaining_instructions

# Checks if a robot has at least two microchips
def robot_has_two_chips(id, robots):
    if robots.get(id):
        if len(robots[id]) >= 2:
            return True
    
    return False

# Returns the lowest and highest value microchips a robot has
def get_low_and_high(id, robots):
    values = sorted(int(chip) for chip in robots[id])
    
    return str(min(values)), str(max(values))

# Adds a microchip to a robot or an output bin
def transfer_microchip(value, id, var_dict):
    if var_dict.get(id):
        var_dict[id].append(value)
    else:
        var_dict.update({id: [value]})
    
    return var_dict

# Transfers a microchip to a robot.
def transfer_microchip_to_robot(value, index, instruction, robots_dict):
    if 'output' not in instruction[index]:
        robots_dict = transfer_microchip(value, instruction[index], robots_dict)

    return robots_dict

def get_required_robot(robots):
    for key, chips in robots.items():
        if '61' in chips and '17' in chips: 
            return key
    return None

# Processes the instructions to distribute microchips among robots and output bins
def simulate_robot_swaps(instructions, robots):
    i = 0 
    
    while i < len(instructions):
        
        for instruction in instructions:

            if robot_has_two_chips(instruction[0], robots):
                low, high = get_low_and_high(instruction[0], robots)

                robots = transfer_microchip_to_robot(low, 2, instruction, robots)
                robots = transfer_microchip_to_robot(high, 4, instruction, robots)

                robots[instruction[0]].remove(low)
                robots[instruction[0]].remove(high)

                required_robot = get_required_robot(robots)
                
                if required_robot:
                    return required_robot
        i += 1
              
#________Main Program_________ # 
if __name__ == "__main__": 
    
    my_instructions = read_file_return_2D_list('text.txt')

    my_robots, my_instructions = get_microchips_from_input_bins(my_instructions)

    answer = simulate_robot_swaps(my_instructions, my_robots)

    print(f'The answer to part one is: {answer}')