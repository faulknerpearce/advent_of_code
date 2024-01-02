# Reads from an input file and returns a list splitting at newlines.
def read_file_return_list(file):
    with open(file) as data:
        lines = [line for line in data.read().split()]
    return lines

def get_outer_inner_strings(line):
    outside_strings = []
    inner_strings = []
    end = len(line)
    idx = 0

    for i in range(end):
        if line[i] == '[':
            outside_strings.append(line[idx:i])
            outside = False
            idx = i + 1
        elif line[i] == ']':
            inner_strings.append(line[idx:i])
            outside = True
            idx = i + 1
        elif i == end - 1 and outside:
            outside_strings.append(line[idx:end])
    
    return outside_strings, inner_strings

def has_valid_pair(str):
    if str[0] == str[1] or str[2] == str[3]:
        return False
    return str[0] == str[3] and str[1] == str[2]

def has_valid_pair_in_window(s):
    for i in range(len(s) - 3):
        if has_valid_pair(s[i:i+4]):
            return True
    return False

def strings_have_a_pair(outer_strings):   
    return any(has_valid_pair_in_window(str) for str in outer_strings)

def part_one(lines):
    count = 0
    for line in lines:
        outer_strings, inner_strings = get_outer_inner_strings(line)

        if strings_have_a_pair(outer_strings) and not strings_have_a_pair(inner_strings):
            count+=1
     
    return count 
            
#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_list('test.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')