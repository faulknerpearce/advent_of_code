import hashlib

# This will check if the generated has has the required number of leading zeros. 
def check_hash(_hash_hex, _difficulty):
    for num in _hash_hex[:_difficulty]: 
        if num != '0':
            return False
    return True

# This will generate a hash with the provided input text and the nonce. 
def generate_hash(_text, _nonce):
    contents = str(_text) + str(_nonce)
    hash = hashlib.md5(contents.encode())
    hash_hex = hash.hexdigest()
    return hash_hex

# This will call the generate_hash and check_hash function and increment the once until the required amount of leading zeros are found. 
def pow(_text, _difficulty):
    nonce = 0
    result = False
    while result != True:
        nonce += 1
        hash = generate_hash(_text, nonce)
        result = check_hash(hash, _difficulty)
    return hash, nonce

# Main Program. 
puzzle = 'yzbqklnj'
difficulty = 4

result_hash, result_nonce = pow(puzzle, difficulty)
print(f'The result hash is: {result_hash}\n The result nonce is: {result_nonce}')









    




