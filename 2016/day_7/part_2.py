from part_1 import read_file_return_list, get_outer_and_inner_strings

# Determines if any outer string contains a three-character sequence with a corresponding reversed sequence in inner strings.
def has_three_character_sequence(outer_strings, inner_strings):
    for string in outer_strings:
        for i in range(len(string) - 2):
            characters = string[i:i+3]

            if characters[0] == characters[2] and characters[0] != characters[1]:
                if has_reversed_sequence(characters, inner_strings):
                    return True
    return False

# Checks if the reversed pattern of a three-character sequence exists in any of the inner strings.
def has_reversed_sequence(pattern, inner_strings):
    inverse = pattern[1] + pattern[0] + pattern[1]

    for string in inner_strings:
        if inverse in string:
            return True
    return False

# Counts the number of strings that meet the condition of having a valid three-character sequence.
def part_two(strlines):
    count = 0
    for string in strlines:
        outer_strings, inner_strings = get_outer_and_inner_strings(string)
        
        if has_three_character_sequence(outer_strings, inner_strings):
            count += 1
    
    return count

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input)
    
    print(f'The answer to part two is: {answer}')