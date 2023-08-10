# This function formats the content of a text file to a string. 
def format_string():
    file = open("text.txt", "r")
    text = file.read()
    file.close()
    return text

# This function will takes a string that contains numbers and format them to a list of integers.
def format_ints():
    i = 0
    temp = ""
    int_list = []
    my_string = format_string()
    while i < len(my_string):
        # Check if the current character is neither 'x' nor a newline
        if my_string[i] != "x" and my_string[i] != "\n":
            temp += my_string[i]
            i += 1
        else:
            int_list.append(int(temp))
            temp = ""
            i += 1   
    # Append the last integer to the list after the loop ends
    int_list.append(int(temp))
    return int_list

# This function compares 3 numbers and multiplys the 2 smallest numbers.  
def get_slack_total(l, w, h):
    numbers = [l, w, h]
    numbers.remove(max(numbers))
    slack_total = numbers[0] * numbers[1]
    return slack_total

# Calculates and returns the total ribbon length needed for a box 
def get_ribbon_total(l, w, h):
    numbers = [l, w, h]
    bow = l * w * h
    numbers.remove(max(numbers))
    ribbon = numbers[0] * 2 + numbers[1] * 2
    ribbon_total = ribbon + bow
    return ribbon_total
    
# This function calculates the total wrapping paper and ribbon needed for a list of boxes with given dimensions.
def box_dimesions(numbers):
    i = 0 
    total_wrapping_paper = 0 
    total_ribbon = 0
    while i < len(numbers):
        # get the box dimensions and calculate the area of the box 
        length = numbers[i]
        width = numbers[i+1]
        hight = numbers[i+2]
        i += 3
        box = (2 * length * width) + (2 * length * hight) + (2 * width * hight)
        # Calculate the slack needed
        slack = get_slack_total(length, width, hight)
        # Calculate the total ribbon needed 
        ribbon = get_ribbon_total(length, width, hight)
        # Calculate the box area pluss the slack and add it to the total wrapping paper. 
        total_wrapping_paper += box + slack 
        total_ribbon += ribbon
    
    return total_wrapping_paper, total_ribbon

my_numbers = format_ints()

my_wrapping_total, my_ribbon_total = box_dimesions(my_numbers)

print("The required amount of warpping paper is: " + str(my_wrapping_total) + " feet. And the required amount of ribbon is: " + str(my_ribbon_total))

