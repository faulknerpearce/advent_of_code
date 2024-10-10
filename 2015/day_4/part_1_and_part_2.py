from hashlib import md5

# Check if the generated hash has the required number of leading zeros.
def check_hash(hash, difficulty):
    return hash[:difficulty] == '0' * difficulty

# Generate a hash with the provided input messaeg and the nonce. 
def generate_hash(message, nonce):

    contents = str(message) + str(nonce) 
    hash = md5(contents.encode()).hexdigest()

    return hash

# Generates Hashes until a hash with the required amount of leading zeros has been found.
def find_hash(message, difficulty):
    nonce = 0
    found = False

    while not found:
        nonce += 1
        new_hash = generate_hash(message, nonce)
        found = check_hash(new_hash, difficulty)

    return nonce

if __name__ == '__main__':
    
    puzzle_input = 'yzbqklnj'

    answer = find_hash(puzzle_input, 6)

    print(f'The answer for part one is: {answer}' )
    