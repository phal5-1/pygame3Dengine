from array import array

def Square(i):
    return i * i

class VectorArray:
    def __init__(self):
        self.datas = array("f")
    
    def Append(self, x, y, z):
        self.datas += array("f", (x, y, z))
    
    def Nullify(self, index: int):
        index *= 3
        self.datas[index] = 0
        self.datas[index + 1] = 0
        self.datas[index + 2] = 0
        
    def Scale(self, index: int, scale: float):
        index *= 3
        self.datas[index] *= scale
        self.datas[index + 1] *= scale
        self.datas[index + 2] *= scale
        
    def Copy(self, copy_to: int, other, copy_from: int):
        copy_from *= 3
        copy_to *= 3
        self.datas[copy_to] = other.datas[copy_from]
        self.datas[copy_to + 1] = other.datas[copy_from + 1]
        self.datas[copy_to + 2] = other.datas[copy_from + 2]
        
    def Add(self, add_to: int, other, add_this: int, scale: float = 1):
        add_to *= 3
        add_this *= 3
        self.datas[add_to] += other.datas[add_this] * scale
        self.datas[add_to + 1] += other.datas[add_this + 1] * scale
        self.datas[add_to + 2] += other.datas[add_this + 2] * scale
        
    def SetDifference(self, index0: int, a, index1: int, b, index2: int, scale):
        index0 *= 3
        index1 *= 3
        index2 *= 3
        self.datas[index0] = (a.datas[index1] - b.datas[index2]) * scale
        self.datas[index0 + 1] = (a.datas[index1 + 1] - b.datas[index2 + 1]) * scale
        self.datas[index0 + 2] = (a.datas[index1 + 2] - b.datas[index2 + 2]) * scale
        
    def SqrMag(self, index):
        index *= 3
        return Square(self.datas[index]) + Square(self.datas[index + 1]) + Square(self.datas[index + 2])
    
    def DistSqrMag(self, index0: int, other, index1: int):
        index0 *= 3
        index1 *= 3
        return Square(self.datas[index0] - other.datas[index1]) + Square(self.datas[index0 + 1] - other.datas[index1 + 1]) + Square(self.datas[index0 + 2] - other.datas[index1 + 2])
    
    def Dot(self, index0: int, other, index1: int):
        index0 *= 3
        index1 *= 3
        return self.datas[index0] * other.datas[index1] + self.datas[index0 + 1] * other.datas[index1 + 1] + self.datas[index0 + 2] * other.datas[index1 + 2]
    
    def SetCross(self, index0: int, a, index1: int, b, index2: int, scale):
        index0 *= 3
        index1 *= 3
        index2 *= 3
        self.datas[index0] = a.datas[index1 + 1] * b.datas[index2 + 2] - a.datas[index1 + 2] * b.datas[index2 + 1]
        self.datas[index0 + 1] = a.datas[index1 + 2] * b.datas[index2] - a.datas[index1] * b.datas[index2 + 2]
        self.datas[index0 + 2] = a.datas[index1] * b.datas[index2 + 1] - a.datas[index1 + 1] * b.datas[index2]
        
    