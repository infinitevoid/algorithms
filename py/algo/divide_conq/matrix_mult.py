from typing import Tuple
"""
You should use numpy!!!

strassen matrix multiplication for 2^n x 2^n matrices
"""

class NNMatrix:
    def __init__(self, target, dim: int, top: int = 0, left: int = 0):
        self.target = target
        self.dim  = dim
        self.top,self.left  = top,left
    @staticmethod
    def Zero(dim: int):
        row = [0 for j in range(dim)]
        mat = [row[:] for i in range(dim)]
        return NNMatrix(mat, dim)
    def __getitem__(self, pos: Tuple[int,int]):
        i,j = pos
        return self.target[self.top+i][self.left+j]
    def __setitem__(self, pos: Tuple[int, int], val):
        i,j = pos
        self.target[i+self.top][j+self.left] = val
    def cut(self, top: int, left: int, dim: int):
        return NNMatrix(self.target, dim, self.top+top, self.left+left)
    def paste(self, mat, top: int, left: int):
        for i in range(mat.dim):
            for j in range(mat.dim):
                self[top+i, left+j] = mat[i,j]
    def add(self, other, target):
        for i in range(self.dim):
            for j in range(self.dim):
                target[i,j] = self[i,j] + other[i,j]
    def sub(self, other, target):
        for i in range(self.dim):
            for j in range(self.dim):
                target[i,j] = self[i,j] - other[i,j]
    def naive_mult(self, other, target):
        for i in range(self.dim):
            for j in range(self.dim):
                sum = 0
                for r in range(self.dim):
                    sum += self[i,r] * other[r,j]
                target[i,j] = sum
    def __add__(self,other):
        target = NNMatrix.Zero(self.dim)
        self.add(other, target)
        return target
    def __sub__(self,other):
        target = NNMatrix.Zero(self.dim)
        self.sub(other, target)
        return target
    def __mul__(self,other):
        target = NNMatrix.Zero(self.dim)
        self.naive_mult(other, target)
        return target


def strassen_mult(X, Y):
    n = X.dim
    if n <=2:
        return X*Y
    assert(n%2) # is currently only implemented for 2^n sized matrices
    mid = n//2
    a,b,c,d = X.cut(0,0,mid), X.cut(0,mid,mid), X.cut(mid,0,mid), X.cut(mid,mid,mid)
    e,f,g,h = Y.cut(0,0,mid), Y.cut(0,mid,mid), Y.cut(mid,0,mid), Y.cut(mid,mid,mid)
    p1 = strassen_mult(a, f - h)
    p2 = strassen_mult(h, a + b)
    p3 = strassen_mult(e, c + d)
    p4 = strassen_mult(d, g - e) 
    p5 = strassen_mult(a + d, e + h)
    p6 = strassen_mult(b - d, g + h)
    p7 = strassen_mult(a - c, e + f)
    result = NNMatrix.Zero(n)
    result.paste(p4 + p5 + p6 - p2, 0, 0)
    result.paste(p1 + p5 - p3 - p7, mid, mid)
    result.paste(p1 + p2, 0, mid)
    result.paste(p3 + p4, mid, 0)
    return result

"""
###Test###
if __name__ == "__main__":
    a = NNMatrix.Zero(3)
    a[0,0] = 1
    a[2,2] = 2
    print(a.target)
    b = a.cut(1,1,2)
    b[0,0] = 3
    print(a.target)
    print((b-b).target)

    a = NNMatrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],4)
    print(strassen_mult(a,a).target)
    print((a*a).target)
"""