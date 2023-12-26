# Reads a file and returns an array of numbers.
def read_file_return_list(file):
    with open(file) as data:
        array = [int(num) for num in data.read().split()]
    return array

def count_possible_triangles(lines):
    count = 0
    for i in range(0, len(lines), 3):
        a, b, c = lines[i], lines[i+1], lines[i+2]
        if (a + b > c) and (a + c > b) and (b + c > a):
            count += 1
    return count

#________Main Program_________ # 
my_input = read_file_return_list('text.txt')

print(count_possible_triangles(my_input))

