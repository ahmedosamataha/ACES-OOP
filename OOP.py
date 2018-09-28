import itertools
counter = itertools.count()
class Matrix:
    id_generator = itertools.count(0)

    def __init__(self, row1):
        self.row1 = row1
        self.id = next(self.id_generator)
    def rows(self):
        return len(self.row1)
    def cols(self):
        return len(self.row1[0])
    def dimensions(self) :
        return '{} * {}' .format(self.rows(),self.cols())
    def description(self):
        print( *self.row1, sep = "\n" )
    def matrix(self):
        a =([0])
        print (a)
    def get_id(self):
        return self.id
A = Matrix([[1,2,3],[3,4,5],[5,6,7]])
B = Matrix([[1,2,3],[2,4,5]])
print(A.rows())
print(A.cols())
print(A.dimensions())
print(A.get_id())
print(A.description())
print(A.matrix())
