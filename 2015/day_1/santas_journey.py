
# This function converts a file to a string 
def convert_to_string():
    with open("text.txt") as file:
        text = file.read()
    return text

# This function seperates string into a list of characters
def convert(my_string):
    my_list = []
    for my_char in my_string:
        if my_char == " ":
            continue
        else: 
            my_list.append(my_char)
    return my_list

# This function will return the floor santa must go to and returns the index of the list that brings santa to the basement. 
def floor_count(my_chars):
    floor = 0
    position = 0
    breaker = 0 
    while position < len(my_chars):
        if my_chars[position] == "(":
            floor += 1
            position += 1
        else:
            floor -= 1
            position += 1

        if floor == -1 and breaker != 1: 
            basement_position = position 
            breaker += 1 
        
    return floor, basement_position

# Main script
my_text = convert_to_string()
chars = convert(my_text)
floors, basement = floor_count(chars)

print("Santans Floor:  " + str(floors) + "\n" + "Basement position: " + str(basement))