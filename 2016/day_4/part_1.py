import re

def read_file_return_2D_list(file):
    '''Reads a file and returns a two dimensional list'''
    with open(file) as text:
        format_one = re.sub(r'|]', '', text.read())
        instructions = [line.split() for line in format_one.replace('[', ' ').split('\n')]
    return instructions

def letter_frequencies(letters):
    '''Returns the frequency of each letter in a given string.'''
    frequencies = {}

    for letter in letters:
        if letter.isalpha():
            if frequencies.get(letter):
                frequencies[letter] += 1
            else:
                frequencies.update({letter: 1})
    return frequencies

def get_most_frequent_letter(letters_dict):
    '''Returns the letter with the highest frequency in the given dictionary of letter frequencies.'''
    max_count = 0
    max_key = ''

    for key in letters_dict.keys():
        if letters_dict[key] > max_count:
            max_count = letters_dict[key]
            max_key = key 
    return max_key, max_count

def remove_letters(tied_letters, letters_dict):
    '''Removes specified letters from the given dictionary of letter frequencies.'''
    for letter in tied_letters:
        letters_dict.pop(letter)

    return letters_dict

def get_tied_letters(max_key, max_val, letters_dict):
    '''Identifies all letters that have the same frequency as the given maximum frequency.'''
    ties = [max_key]
    
    for key in letters_dict.keys():
        if letters_dict[key] == max_val and key != max_key:
            ties.append(key)
    return ties

def get_room_password(possible_room, checksum): 
    '''Generates the room password based on the frequency of letters and the given checksum.'''
    ltr_dict = letter_frequencies(possible_room)
    password = ''
    
    while len(password) < len(checksum):

        letter, value = get_most_frequent_letter(ltr_dict)
        tied_letters = get_tied_letters(letter, value, ltr_dict)
        ltr_dict = remove_letters(tied_letters, ltr_dict)
        password += ''.join(sorted(tied_letters))
    return password[:5]

def part_one(instructions):
    '''Calculates the sum of the valid room numbers based on the room passwords and checksums.'''
    total = 0 

    for instruction in instructions:
        room_checksum = instruction[1]
        room_password = get_room_password(instruction[0], room_checksum)
        
        if room_password == room_checksum:
            room_number = int(instruction[0][-3:])
            total += room_number
    return total 

# Event: https://adventofcode.com/2016/day/4
if __name__ == '__main__':

    puzzle_input = read_file_return_2D_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')