from machine import MachineConfig
import re 

def read_file_return_2d_list(file):
    '''Reads input file, processes text, and returns a 2D list of integers grouped in sets of 3 lines.'''
    instructions = []
    with open(file) as data:

        text = re.sub(r'Button|Prize|A|B|:|X|,|Y|\+|=', '', data.read())
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        for i in range(0, len(lines), 3):
            group = [int(num) for line in lines[i:i+3] for num in line.split()]
            instructions.append(group)

    return instructions

def gcd(a, b):
    '''Computes the greatest common divisor ( GCD ) using Euclid's algorithm.'''
    if b == 0:
        return a
    
    return gcd(b, a % b) 

def is_divisible_by_gcd(prize_x, denominator):
    '''Checks if a number is divisible by the GCD of another number.'''
    return prize_x % denominator == 0

def determinant(x1, x2, y1, y2):
    '''Computes the determinant of a 2x2 matrix.'''
    return (x1 * y2) - (y1 * x2)
  
def press_count(claw_machine, det):
    '''Calculates the number of button presses required based on determinants.'''
    det_n = determinant(claw_machine.prize.x, claw_machine.prize.y, claw_machine.b.movement.x, claw_machine.b.movement.y)
    det_m = determinant(claw_machine.a.movement.x, claw_machine.a.movement.y, claw_machine.prize.x, claw_machine.prize.y)

    if det == 0 or det_n % det != 0 or det_m % det != 0:
        return -1, -1  
    
    n = det_n // det
    m = det_m // det

    return n, m

def calculate_cost(machine, n, m):
    '''Calculates the total cost based on the number of button presses and machine costs.'''
    if n >= 0 and m >= 0 and (n > 0 or m > 0):
        return (machine.a.cost * n) + (machine.b.cost * m)
    
    return 0 

def get_token_count(claw_machine):
    '''Computes the minimum tokens required to win a prize, or returns 0 if unreachable.'''
    gcd_x = gcd(claw_machine.a.movement.x, claw_machine.b.movement.x)
    gcd_y = gcd(claw_machine.a.movement.y, claw_machine.b.movement.y)

    divisible_x = is_divisible_by_gcd(claw_machine.prize.x, gcd_x)
    divisible_y = is_divisible_by_gcd(claw_machine.prize.y, gcd_y)

    if divisible_x and divisible_y:
        
        det = determinant(claw_machine.a.movement.x, claw_machine.b.movement.x, claw_machine.a.movement.y, claw_machine.b.movement.y)

        if det == 0:
            return 0
       
        n, m = press_count(claw_machine, det)

        if n >= 0 and m >= 0:
            return calculate_cost(claw_machine, n, m)
        
    return 0
    
def part_one(instructions):
    '''Processes instructions to compute the total cost for each possible prize.'''
    total = 0 

    for instruction in instructions:

        claw_machine = MachineConfig(instruction[0], instruction[1], instruction[2], instruction[3], instruction[4], instruction[5])

        total += get_token_count(claw_machine)

    return total

# Event: https://adventofcode.com/2024/day/13
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_one(puzzle_input)

    print(f"The answer to part one is: {answer}")
