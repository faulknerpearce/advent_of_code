class Guard:
    '''Guard class initialised with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.distinct_positions = set() 
        self.row = row
        self.col = col
    
    def traverse_row(self, array, move_up):
        '''Traverse through rows, moving up or down'''
        for i in range(1, len(array)):

            if move_up:
                if self.row-i == -1:
                    return True
        
                elif array[self.row-i][self.col] == '#':
                    self.row = (self.row - (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row-i, self.col))
                    
            else:
                if self.row+i == len(array):
                    return True
            
                elif array[self.row+i][self.col] == '#':
                    self.row = (self.row + (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row+i, self.col))

    
    def traverse_col(self, array, move_left):
        '''Traverse through columns, moving left or right'''
        for i in range(1, len(array)):

            if move_left:
                if self.col-i == -1:
                    return True
            
                elif array[self.row][self.col-i] == '#':
                    self.col = (self.col - (i-1))
                    return False 
                else:
                    self.distinct_positions.add((self.row, self.col-i))

            else:
                if self.col+i == len(array):
                    return True
                
                elif array[self.row][self.col+i] == '#':
                    self.col = (self.col + (i-1))
                    return False
                else:
                    self.distinct_positions.add((self.row, self.col+i))