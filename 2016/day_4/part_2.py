from part_1 import read_file_return_2D_list

# Decrypts a string by shifting each letter by a specified number of positions in the alphabet.
def decrypt_string(string, decryption_num):
    decrypted = ''

    for i in range(len(string)):

        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            adjusted_val = ord(string[i]) - 97
            decrypted += chr(((adjusted_val + int(decryption_num)) % 26) + 97) 
        else:
            decrypted += string[i]

    return decrypted

# Finds and returns the room ID for the room containing 'northpole' in its decrypted name.
def get_room_id(instructions):

    for instruction in instructions:
        room_id = instruction[0][-3:]
        decrypted = decrypt_string(instruction[0], room_id) 

        if 'northpole' in decrypted:
            return room_id

if __name__ == '__main__':

    puzzle_input = read_file_return_2D_list('text.txt')

    answer = get_room_id(puzzle_input)

    print(f'The answer for part two is: {answer}')