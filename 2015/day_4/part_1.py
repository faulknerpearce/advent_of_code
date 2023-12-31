import hashlib

# This will check if the generated has has the required number of leading zeros. 
def check_hash(_hash_hex, difficulty):
    for num in _hash_hex[:difficulty]:
        if num != '0':
            return False
    return True

# This will generate a hash with the provided input text and the nonce. 
def generate_hash(_text, _nonce):
    contents = str(_text) + str(_nonce)
    my_hash = hashlib.md5(contents.encode())
    hash_hex = my_hash.hexdigest()
    return hash_hex

# This will call the generate_hash and check_hash function and increment the once until the required amount of leading zeros are found. 
def find_hash(_text, the_difficulty):
    nonce = 0
    result = False
    while result is not True:
        nonce += 1
        new_hash = generate_hash(_text, nonce)
        result = check_hash(new_hash, the_difficulty)
    return new_hash, nonce

#________Main Program_________ # 
if __name__ == "__main__":
    
    my_puzzle = 'yzbqklnj'
    my_difficulty = 4

    result_hash, result_nonce = find_hash(my_puzzle, my_difficulty)
    print(f'The result hash is: {result_hash}\n The result nonce is: {result_nonce}')









    




