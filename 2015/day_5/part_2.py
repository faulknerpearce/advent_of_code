from part_1 import read_file_return_2d_list

# Checks for at least two pairs of letters.
def has_two_pairs(string): 
    for i in range(0, len(string) - 1, 1):
        
        if string[i:i+2] in string[i+1:]:
            return True   
    return False  

# Checks for two repeating letters that have one letter in between them. 
def has_repeating_letter_with_gap(string):
    for i in range(len(string) - 2):
        
        if string[i] == string[i+2] and string[i] != string[i+1]:
            return True 
    return False

# Checks for non-overlapping repeated pairs.
def has_no_overlap(string):
    for i in range(0, len(string) -2, 1):
        if string[i] == string[i+1] and string[i] == string[i+2]:
            return False
    return True

# Count the number of nice strings in a list of lines for the requirements of part two.
def count_nice_strings(my_list):
    count = 0 
    
    for line in my_list:
        
        if has_two_pairs(line) and has_repeating_letter_with_gap(line) and has_no_overlap(line):
            count += 1
    return count

if __name__ == "__main__":

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = count_nice_strings(puzzle_input)

    print(f'The answer for part two is: {answer}')