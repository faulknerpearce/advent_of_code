# Read the contents of a file and return a 2D list, splitting each line into elements.
def read_file_return_2d_list(file):
    with open(file) as text:
        return [line.strip().split() for line in text if line.strip()]

# Retrieve the value from the dictionary if it's a wire (alphabetic), otherwise return the integer value.  
def get_value(item, dict):
    if item.isalpha():
        return dict.get(item, None)
    else: 
        return int(item)   
           
# Assign a value to a key in the dictionary after converting it to an integer.
def assign_value(value, key, bitwise_gates):
    bitwise_gates[key] = int(value)
    return bitwise_gates

# Process AND bitwise operation and assign the result to a wire.
def and_or_gate(a, b, instruction, dict):
    if 'AND' in instruction:
        result = (a & b) & 0xFFFF
    elif 'OR' in instruction:
        result = (a | b) & 0xFFFF

    return assign_value(result, instruction[-1], dict)

# Process NOT bitwise operation and assign the result to a wire.
def not_gate(a, instruction, dict):
    result = ~int(a) & 0xFFFF

    return assign_value(result, instruction[-1], dict)

# Process left or right shift operations and assign the result to a wire.
def shift_gate(a, instruction, dict):
    if 'LSHIFT' in instruction:
        result = (a << int(instruction[2]))
    else:
        result = (a >> int(instruction[2]))

    return assign_value(result, instruction[-1], dict)

# Main function to process all instructions and determine the final state of all wires.
def part_one(instructions):
    bitwise_gates = {}  

    while instructions:
        # Store instructions that can't be processed yet.
        next_pending = []

        for instruction in instructions:

            # Process AND/OR operations.
            if 'AND' in instruction or 'OR' in instruction:
                val_one = get_value(instruction[0], bitwise_gates)
                val_two = get_value(instruction[2], bitwise_gates)

                if val_one is not None and val_two is not None:
                    bitwise_gates = and_or_gate(val_one, val_two, instruction, bitwise_gates)
                else:
                    next_pending.append(instruction)

            # Process NOT operation.
            elif 'NOT' in instruction:
                val = get_value(instruction[1], bitwise_gates)

                if val is not None:
                    bitwise_gates = not_gate(val, instruction, bitwise_gates)
                else:
                    next_pending.append(instruction)

            # Process LSHIFT/RSHIFT operations.
            elif 'LSHIFT' in instruction or 'RSHIFT' in instruction:
                val = get_value(instruction[0], bitwise_gates)

                if val is not None:
                    bitwise_gates = shift_gate(val, instruction, bitwise_gates)
                else:
                    next_pending.append(instruction)

            # Process direct assignment to wire.
            elif instruction[0].isdigit() or instruction[0].isalpha():
                val = get_value(instruction[0], bitwise_gates)

                if val is not None:
                    bitwise_gates = assign_value(val, instruction[-1], bitwise_gates)
                else:
                    next_pending.append(instruction)
        
        # Update pending instructions
        instructions = next_pending

    return bitwise_gates
               
if __name__ == '__main__':

    instructions = read_file_return_2d_list('text.txt')

    gates = part_one(instructions)

    print(gates.get('a'))