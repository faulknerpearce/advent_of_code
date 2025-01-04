from part_1 import read_file_return_2d_list

def has_two_pairs(string):
    '''Checks for at least two pairs of letters.'''
    for i in range(0, len(string) - 1, 1):
        
        if string[i:i+2] in string[i+1:]:
            return True   
    return False  
 
def has_repeating_letter_with_gap(string):
    '''Checks for two repeating letters that have one letter in between them.'''
    for i in range(len(string) - 2):
        
        if string[i] == string[i+2] and string[i] != string[i+1]:
            return True 
    return False

def has_no_overlap(string):
    '''Checks for non-overlapping repeated pairs.'''
    for i in range(0, len(string) -2, 1):
        if string[i] == string[i+1] and string[i] == string[i+2]:
            return False
    return True

def part_two(my_list):
    '''Count the number of nice strings in a list of lines for the requirements of part two.'''
    count = 0 
    
    for line in my_list:
        
        if has_two_pairs(line) and has_repeating_letter_with_gap(line) and has_no_overlap(line):
            count += 1
    return count

# Event: https://adventofcode.com/2015/day/5
if __name__ == "__main__":

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer for part two is: {answer}')