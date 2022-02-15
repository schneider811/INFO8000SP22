from calendar import c
from vector import Vector
#print(vector.a) #cant just use a cus variables dont carry unless file.variable
a_vec = Vector([3,4])
b_vec = Vector([4,5])
#c_vec = Vector(["a","b"])
#print(c_vec.length())
print(str(a_vec))
print(len(a_vec))
print(a_vec.length())
print(Vector.__len__(a_vec))

try:
    c_vec = Vector(["a","b"])
    print(Vector.length(c_vec))
    print(c_vec.length())
except:
    print("Failed to create valid vector")

print(a_vec+b_vec)
d_vec = a_vec.copy()
print(d_vec)
d_vec[0]=90
print(d_vec)