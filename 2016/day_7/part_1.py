# Reads from an input file and returns a list splitting at newlines.
def read_file_return_list(file):
    with open(file) as data:
        strlines = [string for string in data.read().split()]
    return strlines

# Returns outer and inner strings from a line based on brackets.
def get_outer_and_inner_strings(strlines):
    outer_strings = []
    inner_strings = []
    idx = 0

    for i in range(len(strlines)):
        if strlines[i] == '[':
            outer_strings.append(strlines[idx:i])
            outside = False
            idx = i + 1
        elif strlines[i] == ']':
            inner_strings.append(strlines[idx:i])
            outside = True
            idx = i + 1
        elif i == len(strlines) - 1 and outside:
            outer_strings.append(strlines[idx:len(strlines)])
    
    return outer_strings, inner_strings

# Checks if a list of strings contains a pair of characters that form a palindrome.
def has_four_character_sequence(strlines):
    for string in strlines:
        for i in range(len(string) - 3):
            characters = string[i:i+4]
            side_a, side_b = characters[:2], characters[2:]
            if side_a == side_b[::-1] and side_a[0] != side_a[1]:
                return True
    return False

# Counts lines that have a valid pair in outer strings but not in inner strings.
def part_one(strlines):
    count = 0
    for string in strlines:
        outer_strings, inner_strings = get_outer_and_inner_strings(string)

        if has_four_character_sequence(outer_strings) and not has_four_character_sequence(inner_strings):
            count += 1

    return count 
            
#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')

