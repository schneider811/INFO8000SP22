from multiprocessing.sharedctypes import copy


a_list = [3,4,5]
b_list = a_list #copying object not the contents so the two lists become the same see id

b_list[0] = 7
b_list.sort()
print(a_list)
print(id(a_list),id(b_list))

a_num = 3
b_num = a_num
print(id(3))

c_list=b_list.copy() #shallow copy copies element by element but lists can get messy as they will point to each other
c_list[0]=12
print(a_list)
print(c_list)