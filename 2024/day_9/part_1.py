def read_file_return_string(file):
    with open(file) as data:
        string = data.read().strip('\n')

    return string
    
def unpack_file(disk_map):
    disk = ''

    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk += ''.join([str(i - (i // 2)) for _ in range(int(disk_map[i]))])
        else: 
            disk += ''.join(['.' for _ in range(int(disk_map[i]))])

    return disk

def has_space(disk):
    total_spaces = 0
    spaces = 0

    for i in range(len(disk) -1):
        if disk[i] == '.':
            spaces += 1

        if disk[i].isdigit():
            total_spaces +=  spaces
            spaces = 0

    return total_spaces

def get_leftmost(disk):
    for j in range(len(disk)):
        if disk[j] == '.':
            return j

def get_rightmost(disk):
    end = len(disk) -1

    for i in range(end):
        if disk[end-i].isdigit():
            return end-i
        
def compact_disk(disk):
    compacted_disk = list(disk)
    spaces = has_space(disk)

    before = ''.join(disk)

    print(f'\nBefore: {before}\n')

    for _ in range(spaces):

        left_idx = get_leftmost(compacted_disk)
        right_idx = get_rightmost(compacted_disk)

        if left_idx < right_idx:
            compacted_disk[left_idx], compacted_disk[right_idx] = compacted_disk[right_idx], compacted_disk[left_idx]
            test = ''.join(compacted_disk)
            print(f'After Swap: {test}')
            
        else:
            break

    return ''.join(compacted_disk).strip('.')

def get_checksum(disk):
    total = 0
    
    for i in range(len(disk)):
        if disk[i].isdigit():
            total += i * int(disk[i])

    return total
         
if __name__ == '__main__':

    puzzle_input = read_file_return_string('test.txt')

    disk = unpack_file(puzzle_input)

    compacted_disk = compact_disk(disk)

    print(f'\nResult: {compacted_disk}\n')

    answer = get_checksum(compacted_disk)

    print(f'the answer to part one is: {answer}')
