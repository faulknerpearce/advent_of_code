from part_1 import read_file_return_list, get_outer_inner_strings

# Checks if a list of strings contains a pair of characters that form a palindrome.
def strings_have_a_pair(strlines):
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
        outer_strings, inner_strings = get_outer_inner_strings(string)

        if strings_have_a_pair(outer_strings) and not strings_have_a_pair(inner_strings):
            count += 1

    return count

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
