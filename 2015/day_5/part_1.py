# Read lines from a file and return a list of lines
def read_file_retrun_list(file):
    with open(file, 'r') as data:
        text = data.read().split('\n')
        return text

# Checks if a line contains at least three vowels.        
def has_vowels(my_line):
    vowels = 'aeiou'
    count = 0
    for char in my_line:
        if char in vowels:
            count += 1
    if count >= 3: 
        return True 
    else: 
        return False

# Checks for Naughty pairs and return False if any found.
def has_no_naughty_strings(my_line):
    naughty = ['ab', 'cd', 'pq', 'xy']
    last_char = ''
    for letter in my_line:
        combined = last_char + letter 
        if combined in naughty:
            return False
        else: 
            last_char = letter
    return True

# Checks for at least one letter that appears twice in a row.
def has_pair(my_line):
    last = ''
    count = 0
    for char in my_line:
        if last == char: 
            count += 1
        else: 
            last = char
    if count >= 1:
        return True 
    return False 

# Count the number of nice strings in a list of lines for the requirements of part one. 
def count_nice_strings(my_list):
    count = 0
    for line in my_list:
        if has_no_naughty_strings(line) and has_pair(line) and has_vowels(line):
            count += 1
    return count

#________Main Program_________ # 
if __name__ == "__main__":

    my_input = read_file_retrun_list('text.txt')

    answer = count_nice_strings(my_input)

    print(f'The answer for part one is:: {answer}')