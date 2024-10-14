from part_1 import shift_letters, does_not_contain, has_accending, has_two_pairs

# Generates the next valid password.
def part_two(password):
    while True:
        password = shift_letters(password)

        if does_not_contain(password) and has_accending(password) and has_two_pairs(password):
            return ''.join(password)

if __name__ == '__main__':

    puzzle_input = ['h', 'x', 'b', 'x', 'x', 'y', 'z', 'z']
    
    answer = part_two(puzzle_input)

    print(f'The answer to part one is: {answer}')
