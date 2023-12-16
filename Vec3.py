import traceback
import sys

class Vec3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __getitem__(self, index):
        if index == 0: return self.x
        elif index == 1: return self.y
        elif index == 2: return self.z
        
        else:
            traceback.print_stack()
            print('\n' + 'Vec3 access length violation error!')
            sys.exit()
    
    def __str__(self):
        return '(' + self.x + ', ' + self.y + ', ' + self.z + ')'
    
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.x - other.z)
    
    def __mul__(self, scale: float):
        self.x *= scale
        self.y *= scale
        self.z *= scale
        
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
    
    def SetZero(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def Dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def Cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x - other.z, self.x * other.y - self.y * other.x)
    
    def SqrMag(self):
        return self.x * self.x + self.y * self.y + self.x * self.z