# This function formats the content of a text file to a string.
def read_file(file):
    with open(file, encoding='utf-8') as file:
        text = file.read()
    return text

# This will read a string that contains the measurements and format them to a list of integers.
def create_int_array(str_lines):
    temp = ""
    int_list = []
    for i in range(len(str_lines)):
        if str_lines[i] != "x" and str_lines[i] != "\n":
            temp += str_lines[i]
        else:
            int_list.append(int(temp))
            temp = "" 
    int_list.append(int(temp))
    return int_list

# Calculates and returns the total ribbon length needed for a box.
def get_ribbon_total(l, w, h):
    numbers = [l, w, h]
    bow = l * w * h
    numbers.remove(max(numbers))
    ribbon = numbers[0] * 2 + numbers[1] * 2
    ribbon_total = ribbon + bow
    return ribbon_total

# This function calculates the total wrapping paper and ribbon needed for a list of boxes with given dimensions.    
def box_dimesions(numbers):
    total_ribbon = 0
    
    for i in range(0, len(numbers), 3):
        length = numbers[i]
        width = numbers[i+1]
        hight = numbers[i+2]

        ribbon = get_ribbon_total(length, width, hight)
       
        total_ribbon += ribbon
    return total_ribbon

# ________Main Program_________ #
my_input = read_file('text.txt')

my_ints = create_int_array(my_input)

answer = box_dimesions(my_ints)

print(f'The answer to part two is: {answer}')