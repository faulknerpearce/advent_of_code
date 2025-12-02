from part_1 import read_file_return_2d_list, get_starting_position, is_valid_state, eligible_position
import heapq

def breath_first_search(start_row, start_col, matrix):
    '''Uses BFS with a priority queue to find the minimum score path from 'S' to 'E'.'''
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    queue = [(0, start_row, start_col, 'E', [])]  
    visited = {}

    while queue:
        cur_score, cur_row, cur_col, cur_direction, path = heapq.heappop(queue)

        cur_path = path + [(cur_row, cur_col)]

        if matrix[cur_row][cur_col] == 'E':
            return cur_path

        new_row = cur_row + directions[cur_direction][0]
        new_col = cur_col + directions[cur_direction][1]

        if is_valid_state(new_row, new_col, matrix) and eligible_position(cur_score + 1, new_row, new_col, cur_direction, visited):
            
            visited[(new_row, new_col, cur_direction)] = cur_score + 1
            heapq.heappush(queue, (cur_score + 1, new_row, new_col, cur_direction, cur_path))

        for direction in directions.keys():
            if direction != cur_direction and eligible_position(cur_score + 1000, cur_row, cur_col, direction, visited):
                
                visited[(cur_row, cur_col, direction)] = cur_score + 1000
                heapq.heappush(queue, (cur_score + 1000, cur_row, cur_col, direction, cur_path))

    return None

def part_two(steps):
    total = 2
    visited = set()

    for step in steps:

        if step not in visited:
            total += 1
            visited.add(step)

    return total

if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('test.txt')

    starting_row, starting_col = get_starting_position(puzzle_input)

    best_path = breath_first_search(starting_row, starting_col, puzzle_input)

    answer = part_two(best_path)

    print(f'The answer to part two is: {answer}')

