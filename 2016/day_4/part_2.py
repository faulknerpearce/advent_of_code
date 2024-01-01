from part_1 import read_file_return_2D_list, generate_checksum

# Filters out decoy lines based on the correctness of the generated checksum
def remove_decoys(lines):
    valid = []

    for i in range(len(lines)):
        checksum = generate_checksum(lines[i])
        if checksum == lines[i][-1]:
            valid.append(lines[i])
    return valid

# Decrypts a string using a Caesar cipher with a shift based on the second last element of the line.
def decrypt_string(line):
    decryption_id = int(line[-2])
    string = ''

    for characters in line[:-2]:
        for character in characters:
            letter_val = ord(character) - 97
            adjusted_val = (decryption_id + letter_val) % 26
            string += chr(adjusted_val + 97)

        string += ' '

    return string[:-1]

# Returns the ID of the decrypted string that containing the word northpole.
def part_two(lines):

    for line in lines:
        decrypted_string = decrypt_string(line)
        if 'northpole' in decrypted_string:
            return line[-2]

# ________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_2D_list('text.txt')

    puzzle_input = remove_decoys(puzzle_input)

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')
