from part_1 import check_hash, generate_hash

# Returns an 8-character password based on specific positions and characters from qualifying hashes.
def get_password(message):
    password = [0,0,0,0,0,0,0,0] 
    assigned = []
    nonce = 0

    while len(assigned) < len(password): 
        hash_hex = generate_hash(message, nonce)
        
        if check_hash(hash_hex, 5):
            try:
                index = int(hash_hex[5])
                print(f'Current Index {index}')
                print(f'Current Letter {hash_hex[6]}')
                print(f'Current Hash {hash_hex[:7]}')
                
                if index >= 0 and index < len(password) and index not in assigned:  
                    password[index] = hash_hex[6]
                    assigned.append(index)
                    print(f'\nUpdated Password: {password}\n')
            
            except ValueError:
                pass     
        nonce += 1
    
    return ''.join(str(char) for char in password) 

#________Main Program_________ #
if __name__ == "__main__":

    puzzle_input = 'ffykfhsq'

    answer = get_password(puzzle_input)

    print(f'The answer to part two is: {answer}')


    
   
