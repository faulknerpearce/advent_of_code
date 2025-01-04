def read_file_return_2d_list(file):
    '''Read from a file and returns a 2d list.'''
    with open(file) as text:
        instructions = [line.strip('\n') for line in text.readlines()]
        return instructions

def has_vowels(string):
    '''Checks if a string contains at least three vowels.'''
    vowels = 'aeiou'
    count = 0

    for letter in string:
        if letter in vowels:
            count += 1
    return count >= 3

def has_double_letter(string):
    '''Returns true if a string contains one letter that appears twice in a row, and does not contain any naughty pairs.'''
    naughty_letters = ['ab', 'cd', 'pq','xy']
    count = 0

    for i in range(0, len(string) -1, 1):
        
        letters = string[i:i+2]

        if letters in naughty_letters:
            return False
        elif letters[0] == letters[1]:
             count += 1
    return count >= 1

def part_one(strings):
    '''Returns the total number of nice strings.'''
    count = 0

    for string in strings:

        if has_vowels(string) and has_double_letter(string):
            count += 1
    return count

# Event: https://adventofcode.com/2015/day/5
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('test.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')