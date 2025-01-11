def increase_letter(letter):
    '''Increases the given letter by one, wrapping from 'z' to 'a'.'''
    shifted = (1 + (ord(letter) - 97)) % 26

    return chr(shifted + 97)

def get_left_index(password):
    '''Finds the index of the rightmost letter that isn't 'z'''
    for i in range(1, len(password) + 1):
        if password[-i] != 'z':
            return i

def all_equal_z(password):
    '''Checks if all letters in the password are 'z'.'''
    for letter in password:
        if letter != 'z':
            return False
    return True

def add_letter(password):
    '''Resets all letters to 'a' and adds an extra 'a' at the end'''
    for i in range(len(password)):
        password[i] = 'a'
    password.append('a')
    return password

def reset_letters(password):
    '''Creates a new list of 'a's with the same length as the input.'''
    new = []

    for _ in range(len(password)):
        new.append('a')
    
    return new

def shift_letters(password):
    '''Generates the next password in the sequence.'''
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

def has_ascending(password):
    '''Checks if the password contains a straight of at least three increasing letters.'''
    for i in range(0, len(password) -2, 1):
        if ord(password[i]) == ord(password[i+1]) -1 and ord(password[i+1]) == ord(password[i+2]) -1:
            return True
    return False

def get_right_index(letter, password, idx):
    '''Finds the next index where the letter changes.'''
    for i in range(idx, len(password)):
        if password[i] != letter:
            return i -1   
    
    return len(password)

def has_two_pairs(password):
    '''Checks if the password contains at least two different, non-overlapping pairs of letters.'''
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

def does_not_contain(password):
    '''Checks if the password does not contain 'i', 'o', or 'u'.'''
    letters = ['i', 'o', 'u']

    for letter in password:
        if letter in letters:
            return False
    return True

def part_one(password):
    '''Generates the next valid password.'''
    while True:
        password = shift_letters(password)

        if does_not_contain(password) and has_ascending(password) and has_two_pairs(password):
            return ''.join(password)

# Event: https://adventofcode.com/2015/day/11
if __name__ == '__main__':

    puzzle_input = ['h', 'x', 'b', 'x', 'w', 'x', 'b', 'a']
    
    answer = part_one(list('hxbxxyzz'))

    print(f'The answer to part one is: {answer}')
