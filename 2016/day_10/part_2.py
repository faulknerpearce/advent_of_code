from part_1 import read_file_return_2D_list, get_microchips_from_input_bins, simulate_robot_swaps, robot_has_two_chips, get_low_and_high, get_required_robot, transfer_microchip

# Determines whether to transfer a microchip to a robot or an output bin.
def transfer_microchip_to_robot_or_output(value, index, instruction, robots_dict, outputs_dict):
    
    if 'output' in instruction[index]:
        outputs_dict = transfer_microchip(value, instruction[index], outputs_dict)
    else:
        robots_dict = transfer_microchip(value, instruction[index], robots_dict)

    return robots_dict, outputs_dict

# Checks if the required output bins are filled with microchips.
def filled_required_output_bins(outputs):
        return outputs.get('output_0') and outputs.get('output_1') and outputs.get('output_2')

# Calculates the product of values in the first three output bins.
def sum_outputs(outputs):
    val1 = outputs['output_0'][0]
    val2 = outputs['output_1'][0]
    val3 = outputs['output_2'][0]

    return int(val1) * int(val2) * int(val3)

# Processes the instructions to distribute microchips among robots and output bins
def simulate_robot_swaps(instructions, robots, outputs):
    i = 0
    while i < len(instructions): 
        
        for instruction in instructions:
 
            if robot_has_two_chips(instruction[0], robots):

                low, high = get_low_and_high(instruction[0], robots)

                robots, outputs = transfer_microchip_to_robot_or_output(low, 2, instruction, robots, outputs)
                robots, outputs = transfer_microchip_to_robot_or_output(high, 4, instruction, robots, outputs)

                robots[instruction[0]].remove(low)
                robots[instruction[0]].remove(high)

                if filled_required_output_bins(outputs):
                    return sum_outputs(outputs)
        i += 1             
                
#________Main Program_________ # 
if __name__ == "__main__": 

    my_outputs = {}
    
    my_instructions = read_file_return_2D_list('text.txt')

    my_robots, my_remaining_instructions = get_microchips_from_input_bins(my_instructions)

    answer = simulate_robot_swaps(my_remaining_instructions, my_robots, my_outputs)

    print(f'The answer to part two is: {answer}')
    