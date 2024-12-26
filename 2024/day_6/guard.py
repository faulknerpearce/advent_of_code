class Guard:
    '''Guard class initialized with a starting position. used to traverse a matrix, by rows or by columns.'''
    def __init__(self, row, col):
        self.distinct_positions = set() 
        self.row = row
        self.col = col
    
    def traverse(self, row_step, col_step, matrix):
        '''Traverse through rows or columns based on the row and column step.'''
        
        # Row traversal
        if col_step == 0:
            for i in range(self.row + row_step, self.row + (row_step * len(matrix)), row_step):
                
                if i < 0 or i >= len(matrix):
                    return True

                elif matrix[i][self.col] == '#':
                    self.row = i - row_step
                    return False
                
                else:
                    self.distinct_positions.add((i, self.col))
       
        # Column traversal
        else:
            for i in range(self.col + col_step, self.col + (col_step * len(matrix[self.row])), col_step):
                
                if i < 0 or i >= len(matrix[self.row]):
                    return True
            
                elif matrix[self.row][i] == '#':
                    self.col = i - col_step
                    return False
                
                else:
                    self.distinct_positions.add((self.row, i))

        return True