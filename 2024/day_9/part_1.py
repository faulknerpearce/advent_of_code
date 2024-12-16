def read_file_return_string(file):
    '''Reads the input file and returns the content as a string.'''
    with open(file) as data:
        string = data.read().strip('\n')

    return string
 
def unpack_disc(disk_map):
    '''Unpacks the dense disk map into a list of file blocks and free spaces.'''
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk.extend([str(i - (i // 2)) for _ in range(int(disk_map[i]))])
        else: 
            disk.extend(['.' for _ in range(int(disk_map[i]))])

    return disk

def create_file_dict(disk):
    '''Creates a dictionary mapping file block indices to their IDs.'''
    file_dict = {}
    end = len(disk)

    for i in range(len(disk)):

        if disk[-i-1].isdigit():
                file_dict.update({end-i-1: disk[-i-1]})

    return file_dict

def find_free_space(disk):
    '''Finds the index of the leftmost free space.'''
    for j in range(len(disk)):
        if disk[j] == '.':
            return j
        
    return None
  
def compact_disk(disk, file_dict):
    '''Rearranges file blocks to the leftmost free space.'''
    for right_idx in file_dict.keys():

        free_space_idx = find_free_space(disk)

        if free_space_idx is not None and right_idx is not None and free_space_idx < right_idx:
            disk[free_space_idx], disk[right_idx] = disk[right_idx], disk[free_space_idx]    
        else:
            break

    return disk

def get_checksum(disk):
    '''Calculates the checksum as the sum of ( index * file_id) for all file blocks.'''
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
    