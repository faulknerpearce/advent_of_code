import re 
# Reads a file and returns a 2D list after striping specific characters.
def read_file_return_2D_list(file,lines=[]):
    with open(file) as data:
        for string in data.readlines():
            formatted = re.sub(r'-|\[', ' ', string)
            lines.append([line for line in formatted.replace(']', '').split()])

    return lines

# Counts occurrences of each letter in a list of strings.
def count_letters(line):
    letters = {}
    for characters in line:
        for character in characters:
            if letters.get(character):
                letters[character] += 1
            else: 
                letters.update({character: 1})
    return letters

# Sorts a list of letters with equal counts and removes them from the original dictionary.
def unpack(current_ties, current_dict):
    sorted_string = ''
    sorted_letters = sorted(current_ties)
    
    for letter in sorted_letters:
        sorted_string += letter
        current_dict.pop(letter)

    return sorted_string, current_dict

# Finds the key with the greatest value in a dictionary.
def get_greatest_key(my_dict):
    greatest_val = 0
    greatest_key = ''
    
    for key in my_dict.keys():
        if my_dict[key] > greatest_val:
            greatest_key = key
            greatest_val = my_dict[key]
    return greatest_key, greatest_val

# Finds keys in the dictionary that have a value equal to the provided key.
def get_equal_keys(my_dict, best_val):
    ties = []

    for key in my_dict.keys():
        if my_dict[key] == best_val:
           ties.append(key)
    
    if len(ties) > 1:
        return ties 

# Constructs a checksum string based on the frequency and order of letters.
def generate_checksum(line):
    found_letters = ''
    letter_count = count_letters(line[:-2])

    while len(letter_count) > 0:
        max_key, max_val = get_greatest_key(letter_count)

        equal_letters = get_equal_keys(letter_count, max_val)

        if equal_letters:
            letters, letter_count = unpack(equal_letters, letter_count)
            found_letters += letters
        else:
            found_letters += max_key
            letter_count.pop(max_key)

    return found_letters[:len(line[-1])]

def part_one(lines):
    total = 0
    
    for line in lines:
        checksum = generate_checksum(line)
        
        if checksum == line[-1]:
            total += int(line[-2])
    return total

#________Main Program_________ # 
if __name__ == "__main__":
    
    puzzle_input = read_file_return_2D_list('test.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
    