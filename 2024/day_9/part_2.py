def read_file_return_string(file):
    with open(file) as data:
        string = data.read().strip('\n')

    return string
    
def unpack_disk(instructions):
    disk = []
    for i in range(len(instructions)):
        if i % 2 == 0:
            result = [str(i - (i // 2)) for _ in range(int(instructions[i]))]
            number = ''.join(result)
            disk.append(number)   
        else: 
            disk.extend(['.' for _ in range(int(instructions[i]))])
    
    return disk

def create_file_dict(disk):
    file_dict = {}
    end = len(disk)

    for i in range(len(disk)):

        if disk[-i-1].isdigit():
            file_dict.update({disk[-i-1]: end-i-1})

    return file_dict

def get_file_and_index(file_dict):
    for key, value in file_dict.items():
        del file_dict[key]
        return key, value
        
def get_left_index(disk, req_space):
    spaces = 0
    index = None

    for i in range(len(disk)):
        if disk[i] == '.':
            if spaces == 0:  
                index = i
            spaces += 1
            if spaces >= req_space:
                return index 
        else:
            spaces = 0
            index = None

    return None

def swap_elements(right_idx, left_idx, disk):
    req_space = len(disk[right_idx])
    number = disk[right_idx]

    disk = disk[ :right_idx] + ['.'] * req_space + disk[right_idx + 1: ] 
    
    disk = disk[ :left_idx] + list(number) + disk[left_idx + req_space: ]

    return disk

def compact_disk(disk, file_dict):
    for i in range(len(file_dict)):
        
        file_id, file_idx = get_file_and_index(file_dict)

        left_idx = get_left_index(disk, len(file_id))

        if left_idx is not None:
            if left_idx < file_idx :
                disk = swap_elements(file_idx, left_idx, disk)

    return ''.join(disk)

def get_checksum(disk):
    total = 0
    
    for i in range(len(disk)):
        if disk[i].isdigit():

            total += i * int(disk[i])

    return total
         
if __name__ == '__main__':

    puzzle_input = read_file_return_string('test.txt')

    unpacked_disk = unpack_disk(puzzle_input)

    files = create_file_dict(unpacked_disk)

    compacted_disk = compact_disk(unpacked_disk, files)
 
    answer = get_checksum(compacted_disk)

    print(f'the answer to part one is: {answer}')