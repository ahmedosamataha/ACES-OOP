class Matrix:
    def __init__(self, row1, row2, row3, row4):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
A = Matrix([1,2,3],[3,4,5],[5,6,7],[7,8,9])
print(A.row3)   
