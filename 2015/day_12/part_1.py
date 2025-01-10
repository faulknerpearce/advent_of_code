import re 

def read_file_return_list(file):
    with open(file) as data:

        return re.sub(r'\[|\]|\{|\}|:|,|\"', ' ', data.read()).split()
    
def check_element(element):
    if element[0] == '-' and element[1:].isdigit():
        return - int(element[1:])
    
    elif element.isdigit():
        return int(element)

    else:
        return 0
         
def part_one(array):
    total = 0 

    for element in array:
        total += check_element(element)

    return total

if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)
    
    print(f'The answer ot part one is: {answer}')