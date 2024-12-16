# Reads the content of a file and returns it as a string.
def read_file_return_string(file):
    with open(file) as data:
        return data.read().strip('\n')

# Unpacks the dense disk map into a list of file blocks and free spaces. 
def unpack_disc(disk_map):
    disk = []

    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk.extend([str(i - (i // 2)) for _ in range(int(disk_map[i]))])
        else:
            disk.extend(['.' for _ in range(int(disk_map[i]))])
    return disk

# Creates a dictionary mapping file start indices to file IDs.
def create_file_dict(disk):
    file_dict = {}
    end = len(disk)

    for i in range(len(disk)):
        if disk[-i - 1].isdigit():
            file_dict[end - i - 1] = disk[-i - 1]
    
    return file_dict

# Finds the start index and length of a contiguous block for a given file ID.
def find_file_run(disk, file_id):
    index = None
    length = 0

    for i, block in enumerate(disk):
        if block == file_id:
            if index is None:
                index = i
            length += 1
        elif index is not None:
            break
   
    return (index, length) if index is not None else None

 # Finds the start index of a free space block large enough to fit a file.
def find_free_space(disk, file_start, file_length):
    free_space_index = None
    free_length = 0
    
    for i in range(file_start):
        if disk[i] == '.':
            if free_space_index is None:
                free_space_index = i
            free_length += 1
            if free_length >= file_length:
                return free_space_index
        else:
            free_space_index = None
            free_length = 0
    return None

 # Moves a file from its current position to a new free space on the disk.
def move_file(disk, file_start, file_length, free_start):
    file_id = disk[file_start]
    
    disk[file_start:file_start + file_length] = ['.'] * file_length
    
    disk[free_start:free_start + file_length] = [file_id] * file_length
    
    return disk

# Compacts the disk by moving files to the earliest free space available.
def compact_disk(disk, file_dict):
    for file_start, file_id in file_dict.items():
        file_run = find_file_run(disk, file_id)
        
        if file_run:
            start, length = file_run
            free_start = find_free_space(disk, start, length)
            
            if free_start is not None:
                disk = move_file(disk, start, length, free_start)
    
    return disk

 # Calculates the checksum as the sum of index multiplied by file ID value.
def get_checksum(disk):
    return sum(i * int(disk[i]) for i in range(len(disk)) if disk[i].isdigit())

# Event: https://adventofcode.com/2024/day/9 
if __name__ == '__main__':
    
    puzzle_input = read_file_return_string('text.txt')
    
    unpacked_disk = unpack_disc(puzzle_input)
    
    file_dictionary = create_file_dict(unpacked_disk)
    
    compacted_disk = compact_disk(unpacked_disk, file_dictionary)
    
    answer = get_checksum(compacted_disk)
    
    print(f'The answer to part two is: {answer}')
    