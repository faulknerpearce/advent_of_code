# Reads the input file and returns the content as a string.
def read_file_return_string(file):
    with open(file) as data:
        string = data.read().strip('\n')

    return string

# Unpacks the dense disk map into a list of file blocks and free spaces.  
def unpack_disc(disk_map):
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk.extend([str(i - (i // 2)) for _ in range(int(disk_map[i]))])
        else: 
            disk.extend(['.' for _ in range(int(disk_map[i]))])

    return disk

# Creates a dictionary mapping file block indices to their IDs.
def create_file_dict(disk):
    file_dict = {}
    end = len(disk)

    for i in range(len(disk)):

        if disk[-i-1].isdigit():
                file_dict.update({end-i-1: disk[-i-1]})

    return file_dict

# Finds the index of the leftmost free space.
def get_left_index(disk):
    for j in range(len(disk)):
        if disk[j] == '.':
            return j
        
    return None

# Retrieves the index of the rightmost file block and removes it from the dictionary.
def get_right_index(file_dict):
    for key in file_dict.keys():
        del file_dict[key]

        return key
    
    return None

# Rearranges file blocks to the leftmost free space.  
def compact_disk(disk, file_dict):

    for _ in range(len(file_dict)):
        left_idx = get_left_index(disk)
        right_idx = get_right_index(file_dict)

        if left_idx is not None and right_idx is not None and left_idx < right_idx:
            disk[left_idx], disk[right_idx] = disk[right_idx], disk[left_idx]
            
        else:
            break

    return disk

# Calculates the checksum as the sum of ( index * file_id) for all file blocks.
def get_checksum(disk):
    total = 0
    
    for i in range(len(disk)):
        if disk[i].isdigit():
            total += i * int(disk[i])

    return total

# Event: https://adventofcode.com/2024/day/9        
if __name__ == '__main__':

    puzzle_input = read_file_return_string('text.txt')

    disk = unpack_disc(puzzle_input)

    file_dictionary = create_file_dict(disk)

    compacted_disk = compact_disk(disk, file_dictionary)

    answer = get_checksum(compacted_disk)

    print(f'the answer to part one is: {answer}')
    