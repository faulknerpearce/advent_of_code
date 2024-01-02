# Reads a file and returns its content as a list of strings split by whitespace.
def read_file_return_list(file):
    with open(file) as data:
        lines = [line for line in data.read().split()]
    return lines

# Retrieves the letter with the maximum or minimum frequency from a dictionary.
def get_letters(dictionary, get_maximum):
   if get_maximum:
        return max(dictionary, key=dictionary.get)
   else:
        return min(dictionary, key=dictionary.get)

# Constructs a corrected message from a list of strings, using either most or least common letters per column.
def get_error_corrected_message(rows, get_maximum=True):
    message = ''
    letters = {}

    for i in range(len(rows[0])):
        for row in rows:
            if letters.get(row[i]):
                letters[row[i]] += 1 
            else:
                letters.update({row[i]: 1})

        message += get_letters(letters, get_maximum)
        letters = {}

    return message

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer = get_error_corrected_message(puzzle_input)

    print(f'The answer to part one is: {answer}')
