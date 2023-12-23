from part_1 import read_file

# Checks for at least two pairs of letters.
def has_two_pairs(my_line): 
    last = my_line[0] 
    for i in range(len(my_line) - 1):
        if last + my_line[i+1] in my_line[i+1:]:
            return True 
        else:
            last = my_line[i+1]
    return False  

# Checks for two repeating letters that have one letter in between them. 
def has_repeating_letter_with_gap(my_line):
    for i in range(len(my_line) - 2):
        if my_line[i] == my_line[i+2] and my_line[i] != my_line[i+1]:
            return True 
    return False

# Checks for non-overlapping repeated pairs.
def has_no_overlap(my_line):
    prev = my_line[0]
    for i in range(len(my_line) - 2):
        if prev == my_line[i+1]:
            combined = prev + my_line[i+1]
            if combined[0] == my_line[i+2] :
                return False
        prev = my_line[i+1]
    return True

# Count the number of nice strings in a list of lines for the requirements of part two.
def count_nice_strings(my_list):
    count = 0 
    for line in my_list:
        if has_two_pairs(line) and has_repeating_letter_with_gap(line) and has_no_overlap(line):
            count += 1
    return count

# ________Main Program_________ #
my_input = read_file('text.txt')

answer = count_nice_strings(my_input)

print(f'The answer for part two is: {answer}')