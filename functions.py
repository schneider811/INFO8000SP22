#def my_fun(): #can only use functions after function is defined (not in lines above)
#    #pass #tells function/python to do nothing
#    print('hello world')

from cmath import sqrt


def my_fun(to_print):
    print(to_print)
    return None

#my_fun("Hello World")
a = my_fun
a("Hi World")

c = 3+7.545345
print(c)

to_print = f"{c:.2f}"
a("Hello World")
print(to_print)

def pyth(a,b):
    c2 = a**2+b**2
    return sqrt(c2) 

print(pyth(3,4))

def find(a_list,value):
    for i in range(0,len(a_list)):
        if a_list[i] == value:
            return (True, i)
    return(False, None)

a_list = [3,6,2]

print(find(a_list,6))

found,index = find(a_list,8)
print(found,index)