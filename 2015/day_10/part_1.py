# Converts a sequence by counting consecutive digits and outputting the count followed by the digit.
def convert_sequence(numbers):
    count = 1
    converted = ''
   
    for i in range(1, len(numbers)):
        last = numbers[i-1]

        if numbers[i] == last: 
            count += 1
        else:
            converted += str(count) + last
            last = numbers[i]
            count = 1
        
        if i == len(numbers) -1:
            
            converted += str(count) + last

    return converted

# Repeats the conversion process 40 times and returns the length of the final sequence
def part_one(numbers):
    for _ in range(40):
        numbers = convert_sequence(numbers)

    return (len(numbers))

if __name__ == '__main__':

    puzzle_input = '1113222113'

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')