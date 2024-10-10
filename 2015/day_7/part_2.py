from part_1 import read_file_return_2d_list, get_value, and_or_gate, not_gate, shift_gate, assign_value

# Main function to process all instructions and determine the final state of all wires.
def part_two(instructions):
    bitwise_gates = {'b': 956}  

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
                    if instruction[-1] != 'b': 
                        bitwise_gates = assign_value(val, instruction[-1], bitwise_gates)
                else:
                    next_pending.append(instruction)
        
        # Update pending instructions.
        instructions = next_pending

    return bitwise_gates

if __name__ == '__main__':

    instructions = read_file_return_2d_list('text.txt')

    gates = part_two(instructions)

    answer = gates.get('a')

    print(f'The answer to part one is: {answer}.')

    required_answer = '40149'