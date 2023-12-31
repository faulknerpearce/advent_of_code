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

# This function compares 3 numbers and multiplys the 2 smallest numbers.
def get_slack_total(l, w, h):
    numbers = [l, w, h]
    numbers.remove(max(numbers))
    slack_total = numbers[0] * numbers[1]
    return slack_total

# This function calculates the total wrapping paper and ribbon needed for a list of boxes with given dimensions.  
def calculate_total_wrapping_paper(numbers):
    total_wrapping_paper = 0 
    for i in range(0, len(numbers), 3):
        length = numbers[i]
        width = numbers[i+1]
        hight = numbers[i+2]
        
        box = (2 * length * width) + (2 * length * hight) + (2 * width * hight)
        
        slack = get_slack_total(length, width, hight)

        total_wrapping_paper += box + slack

    return total_wrapping_paper

#________Main Program_________ # 
if __name__ == "__main__":
    
    my_input = read_file('text.txt')

    my_ints = create_int_array(my_input)

    answer = calculate_total_wrapping_paper(my_ints)

    print(f'The answer to part one is: {answer}')