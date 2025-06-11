

class matrix:
    def __init__(self, mat):
        self.mat = mat
        self.rows = len(mat)
        self.cols = len(mat[0])

    def cofactor(self, row, col):
        # Adjust indices to zero-based
        row -= 1
        col -= 1
        
        # Initialize an empty list to hold the cofactor matrix
        cofactor_matrix = []
        
        # Iterate through rows of the original matrix
        for i in range(self.rows):
            if i != row:  # Skip the specified row
                new_row = []  # Create a new row for the cofactor matrix
                for j in range(self.cols):
                    if j != col:  # Skip the specified column
                        new_row.append(self.mat[i][j])
                cofactor_matrix.append(new_row)
        
        # Return the cofactor matrix wrapped in a `matrix` object (assuming `matrix` is defined elsewhere)
        return matrix(cofactor_matrix)

# Example matrix
m = matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

# Get cofactor excluding row=2 and col=2
cof = m.cofactor(3, 3)
print(cof.mat)  # Output will be [[1, 3], [7, 9]]
