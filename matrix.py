import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self[0][0]  #determ is a variable that calculates the determinant value
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if (a*d - b*c) == 0:
                raise(ValueError, "Determinant value is invalid")
                
            else:   
                return a*d - b*c
            
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        tr = 0  #calculates trace
        for i in range(self.h):
            tr += self.g[i][i] #calculates trace
        return tr            

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        determ = self.determinant()
        if (self.h == 1):
            inv = [[1/determ]]
        if (self.h == 2):
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            inv = [[d , -b],[-c , a]]
            for i in range(self.h):
                for j in range(self.w):
                    inv.g[i][j] = inv.g[i][j]*(1/determ)
        return Matrix(inv)            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self[j][i])
            transpose.append(row)
        return Matrix(transpose)    

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        add = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            add.append(row)
        return Matrix(add)    

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        new_g = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self[i][j])
            new_g.append(row)    
        return Matrix(new_g)        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        sub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            sub.append(row)
        return Matrix(sub)    

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dot_product(vector_one, vector_two):
            result = 0
    
            for i in range(len(vector_one)):
                result += vector_one[i] * vector_two[i]
            return result
        
        product = []
        trans = other.T()
        
        for i in range(self.h):
            row = []
            for j in range(other.w):
                dot_prod = dot_product(self[i], trans[j])
                row.append(dot_prod)
            
            product.append(row)
    
        return Matrix(product)        
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            n_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self[i][j])
                n_matrix.append(row)
            return Matrix(n_matrix)    
            #   
            # TODO - your code here
            #
            