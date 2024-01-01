from hashlib import md5

# Generates an MD5 hash for a given message concatenated with a nonce.
def generate_hash(message, nonce):
    contents = message + str(nonce)
    new_hash = md5(contents.encode()).hexdigest()
    return new_hash

# Checks if a hash meets a specified difficulty (number of leading zeros).;
def check_hash(hash_hex, difficulty):
    return hash_hex[:difficulty] == '0' * difficulty

# Returns an 8 character password based on the characters at the 6th index of qualifying hashes.
def get_password(message):
    password = ''
    nonce = 0
    
    while len(password) < 8:
        hash_hex = generate_hash(message, nonce)
        
        if check_hash(hash_hex, 5):
            password += hash_hex[5]
        nonce += 1

    return password

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = 'ffykfhsq'

    answer = get_password(puzzle_input)

    print(f'The answer to part one is: {answer}')

   
 