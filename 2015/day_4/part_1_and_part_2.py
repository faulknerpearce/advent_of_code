from hashlib import md5

def check_hash(hash, difficulty):
    '''Check if the generated hash has the required number of leading zeros.'''
    return hash[:difficulty] == '0' * difficulty
 
def generate_hash(message, nonce):
    '''Generate a hash with the provided input message and the nonce.'''
    contents = str(message) + str(nonce) 
    hash = md5(contents.encode()).hexdigest()

    return hash

def find_hash(message, difficulty):
    '''Generates Hashes until a hash with the required amount of leading zeros has been found.'''
    nonce = 0
    found = False

    while not found:
        nonce += 1
        new_hash = generate_hash(message, nonce)
        found = check_hash(new_hash, difficulty)

    return nonce

# Event: https://adventofcode.com/2015/day/4
if __name__ == '__main__':
    
    puzzle_input = 'yzbqklnj'

    answer = find_hash(puzzle_input, 6)

    print(f'The answer for part one is: {answer}' )
    