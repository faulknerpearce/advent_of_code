from part_1 import check_hash, generate_hash

# Returns an 8-character password based on specific positions and characters from qualifying hashes.
def get_password(message):
    password = [0,0,0,0,0,0,0,0] 
    index_used = []
    nonce = 0

    while len(index_used) < 8: 
        hash_hex = generate_hash(message, nonce)
        
        if check_hash(hash_hex, 5):
            try:
                index = int(hash_hex[5])
     
                if index >= 0 and index <= 7 and index not in index_used:  
                    password[index] = hash_hex[6]
                    index_used.append(index)
            
            except: 
                ValueError
                    
        nonce += 1
    
    return ''.join(str(char) for char in password) 

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = 'ffykfhsq'

    answer = get_password(puzzle_input)

    print(f'The answer to part two is: {answer}')
