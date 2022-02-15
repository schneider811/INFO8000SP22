from math import sqrt
class Vector:
    def __init__(self, data):  #first thing to do when creating a class is to initialize an object.
        self.data = data.copy() #Functions within a class is a method outside of class is function
        #self.data = data #does not make a copy and is bad to do
    def __str__(self):
        to_return = ",".join([f"{x:.2f}" for x in self.data])
        return f"<{to_return}>"
        
    def __len__(self):
        return len(self.data)
    def length(self):
        the_sum = 0
        for n in self.data:
            the_sum += n**2
        return sqrt(the_sum)
    def __add__(self,other):
        #self + other
        new_list = [x for x in self.data]
        for i in range(len(new_list)):
            new_list[i] += other.data[i]
        return Vector(new_list)
    def __setitem__(self,location,value):
        self.data[location] = value
    def copy(self):
        return Vector(self.data.copy())