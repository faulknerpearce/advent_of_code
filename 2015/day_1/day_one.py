# This function converts a file to a string 
def read_file():
    with open("text.txt") as file:
        text = file.read()
        return text

# This function will return the floor santa must go to and returns the index of the list that brings santa to the basement. 
def floor_count(my_string):
    floor = 0
    position = 0
    breaker = 0 
    
    for char in my_string:
        if char == "(":
            floor += 1
            position += 1
        else:
            floor -= 1
            position += 1

        if floor == -1 and breaker != 1: 
            basement_position = position 
            breaker += 1 
        
    return floor, basement_position

# Main 
the_string = read_file()

floors, basement = floor_count(the_string)

print("Santans Floor:  " + str(floors) + "\n" + "Basement position: " + str(basement))