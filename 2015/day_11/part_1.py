# Increases the given letter by one, wrapping from 'z' to 'a'.
def increase_letter(letter):
    shifted = (1 + (ord(letter) - 97)) % 26

    return chr(shifted + 97)

# Finds the index of the rightmost letter that isn't 'z'
def get_left_index(password):
    for i in range(1, len(password) + 1):
        if password[-i] != 'z':
            return i

# Checks if all letters in the password are 'z'.
def all_equal_z(password):
    for letter in password:
        if letter != 'z':
            return False
    return True

# Resets all letters to 'a' and adds an extra 'a' at the end
def add_letter(password):
    for i in range(len(password)):
        password[i] = 'a'
    password.append('a')
    return password

# Creates a new list of 'a's with the same length as the input.
def reset_letters(password):
    new = []

    for _ in range(len(password)):
        new.append('a')
    
    return new

# Generates the next password in the sequence.
def shift_letters(password):

    if all_equal_z(password):
        password = add_letter(password)   
    else:
        index = get_left_index(password)
        new_letter = increase_letter(password[-index])
        password[-index] = new_letter

        if index > 1:
            reset = reset_letters(password[-index+1:])
            password = password[:-index+1] + reset

    return password

# Checks if the password contains a straight of at least three increasing letters.
def has_accending(password):
    for i in range(0, len(password) -2, 1):
        if ord(password[i]) == ord(password[i+1]) -1 and ord(password[i+1]) == ord(password[i+2]) -1:
            return True
    return False

# Finds the next index where the letter changes.
def get_right_index(letter, password, idx):
    for i in range(idx, len(password)):
        if password[i] != letter:
            return i -1   
    
    return len(password)

# Checks if the password contains at least two different, non-overlapping pairs of letters.
def has_two_pairs(password):
    count = 0
    i = 0

    while i < len(password) -2:

        if password[i] == password[i+1]:
            if password[i] == password[i+2]:
                i = get_right_index(password[i], password, i)
            else:
                count += 1

        if i == len(password) -3:
            if password[i+1] == password[i+2] and password[i+1] != password[i]:
                count += 1
        i += 1

    return count >= 2

# Checks if the password does not contain 'i', 'o', or 'u'.
def does_not_contain(password):
    letters = ['i', 'o', 'u']

    for letter in password:
        if letter in letters:
            return False
    return True

# Generates the next valid password.
def part_one(password):
    while True:
        password = shift_letters(password)

        if does_not_contain(password) and has_accending(password) and has_two_pairs(password):
            return ''.join(password)

if __name__ == '__main__':

    puzzle_input = ['h', 'x', 'b', 'x', 'w', 'x', 'b', 'a']
    
    answer = part_one(list('hxbxxyzz'))

    print(f'The answer to part one is: {answer}')
