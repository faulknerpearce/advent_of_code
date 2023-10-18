# Read lines from a file and return a list of lines
def read_file():
    with open('text.txt', 'r') as text:
        text_file_raw = text.read()
        text_file = text_file_raw.strip()
        text_lines = text_file.split('\n')
        return text_lines

# Check if a line contains at least three vowels         
def check_vowels(my_line):
    vowels = 'aeiou'
    count = 0
    for char in my_line:
        if char in vowels:
            count += 1
    if count >= 3: 
        return True 
    else: 
        return False

# Check for 'naughty' pairs and return False if any found
def check_for_naughty_strings(my_line):
    naughty = ['ab', 'cd', 'pq', 'xy']
    last_char = ''
    for letter in my_line:
        combined = last_char + letter 
        if combined in naughty:
            return False
        else: 
            last_char = letter
    return True

# Check for consecutive double characters in a line
def check_for_double(my_line):
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

# Count the number of nice strings in a list of lines
def count_nice_strings(my_list):
    nice_list_count = 0
    for line in my_list:
        if check_for_naughty_strings(line) and check_for_double(line) and check_vowels(line):
            nice_list_count += 1
    return nice_list_count

# Main 
the_lines = read_file()
result = count_nice_strings(the_lines)
print(f'The number of nice strings are: {result}')