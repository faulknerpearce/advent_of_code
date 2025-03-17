import json

def read_file_return_json(file):
    with open(file) as data:
        return json.load(data)

def part_two(data):
    stack = [data]
    total = 0

    while stack:
        current = stack.pop()

        if isinstance(current, int):
            total += current
       
        elif isinstance(current, list):
            stack.extend(current)
        
        elif isinstance(current, dict):
            if "red" in current.values():
                continue

            stack.extend(current.values())

    return total

if __name__ == '__main__':
    
    puzzle_input_file = read_file_return_json('text.txt')

    answer_part_two = part_two(puzzle_input_file)
    
    print(f'The answer to part two is: {answer_part_two}')