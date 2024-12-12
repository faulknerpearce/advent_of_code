from itertools import product
from part_1 import read_file_return_2d_list, insert_operators

# Evaluates an arithmetic expression from left to right using given operators.
def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])  

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        
        elif operator == '||':
            result = int((str(result) + str(operand)))

    return result

# Checks if any combination of addition, multiplication, or concatenation can make the array equal to the target.
def check_possible_equations(target, array):
    operators = ['+', '*', '||']

    if len(array) == 2:
        return check_equation(target, array)
    
    else:
        for combination in product(operators, repeat=len(array) - 1):
        
            equation = insert_operators(array, list(combination))
            result = evaluate_left_to_right(equation)

            if result == target:
                return True
        
        return False
    
# Checks if addition, multiplication, or concatenation of two numbers equals the target.
def check_equation(target, numbers):
    return numbers[0] + numbers[1] == target or numbers[0] * numbers[1] == target or int(str(numbers[0]) + str(numbers[1])) == target 

# Calculates the sum of all valid target values in the array for part two.
def part_two(arrays):
    total = 0

    for array in arrays: 
        if check_possible_equations(array[:1][0], array[1:]):
            total += array[:1][0]

    return total

# Event: https://adventofcode.com/2024/day/7
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')
