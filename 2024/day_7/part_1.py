from itertools import product

# Reads a file and converts its content into a 2D list of integers.
def read_file_return_2d_list(file):
    with open(file) as data:
        array = [[int(num) for num in line.replace(':', '').split()] for line in data.readlines()]

    return array

# Evaluates an arithmetic expression from left to right, respecting operation order.
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

    return result

# Inserts operators into an array to create an arithmetic expression as a string.
def insert_operators(array, op):
    result = str(array[0])

    for i in range(len(op)):
        result += f' {op[i]} {str(array[i+1])}'
       
    return result

# Checks if any combination of addition, multiplication results in the target value for the array.
def check_possible_equations(target, array):
    operators = ['+', '*']

    if len(array) == 2:
        return check_equation(target, array)
    
    else:
        for combination in product(operators, repeat=len(array) - 1):
            equation = insert_operators(array, list(combination))
            result = evaluate_left_to_right(equation)

            if result == target:
                return True
        
        return False

# Checks if either addition or multiplication of two numbers equals the target.
def check_equation(target, numbers):
    return (numbers[0] + numbers[1]) == target or (numbers[0] * numbers[1]) == target

# Calculates the total sum of target values where equations can match using valid operators.
def part_one(arrays):
    total = 0

    for array in arrays:
        # Splits the array into target (first element) and numbers (remaining elements),
        if check_possible_equations(array[:1][0], array[1:]):
            total += array[:1][0]

    return total

# Event: https://adventofcode.com/2024/day/7
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
