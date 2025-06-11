class matrix():
    def __init__(self,mat):
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.rowspace = mat
        self.colspace = []
        for i in range(self.cols):
            col = []
            for j in range(self.rows):
                col.append(mat[j][i])
            self.colspace.append(col)
        self.mat = mat
    
    def display(self):
        if self.rows ==1:
            return self.mat[0][0]
        for i in range(self.rows):
            for j in range(self.cols):
                print(f"{self.mat[i][j]}",end=" ")
            print()
        print()
    
    def __add__(self,other):
        d=[]
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.mat[i][j]+other.mat[i][j])
            d.append(row)
        return matrix(d)
    
    def __sub__(self,other):
        d=[]
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.mat[i][j]-other.mat[i][j])
            d.append(row)
        return matrix(d)
    
    def __multiply__(self,other):
        d=[]
        for m in range(self.rows):
            row = []
            for n in range(other.cols):
                a_mn = 0
                for p in range(self.cols):
                    a_mn += self.mat[m][p]*other.mat[p][n]
                row.append(a_mn)
            d.append(row)
        return matrix(d)
    
    def transpose(self):
        return matrix(self.colspace)
    
    def cofactor(self,row,col):
        row -=1
        col-=1
        d=[]
        for i in range(self.rows):
            if i != row:
                new_row=[]
                for j in range(self.cols):
                    if j != col:
                        new_row.append(self.mat[i][j])
                d.append(new_row)
        return matrix(d)
    
    def determinant(self):
        if self.rows == 1:
            return self.mat[0][0]
        if self.rows == 2:
            return self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]

        det = 0
        for i in range(self.cols):
            sign = (-1) ** i
            cofactor = self.cofactor(1, i+1)  # 1-based index
            det += sign * self.mat[0][i] * cofactor.determinant()
        return det

    
    def O(self,n):
        z=[0]*n
        return matrix([z]*n)
    
    def inverse(self):
        if self.rows==2:
            x=matrix(self.cofactor(1,1))
            for i in range(2,3):
                x= x+matrix(self.cofactor(1,i))

        # matrix(self.cofactor(1,i).determinant() for i in range(1,self.rows+1))

A = matrix([[2,3],[1,4]])
# A.display()

B=matrix([[5,2],[3,1]])
# B.display()

# C = A.add(B)
# C.display()
# print(A.colspace)
#D = A.sub(B)
#D.display()
#E = A.multiply(B)
#E.display()
# F = A.transpose()
# F.display()

# G = A.cofactor(2,2)
# G.display()

M = matrix([[1,2],[4,5]])
N = M.cofactor(1,2)
N.display()
# N = M.cofactor(3,1)
# N.display()

# K = A.inverse()
# K.display()

# M = matrix([[1]])
# M.O(4).display()