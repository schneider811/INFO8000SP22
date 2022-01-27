from tracemalloc import stop


print("Loading the file")
f = open("test.txt")
lines = f.readlines()
print(lines)

the_sum = 0

for line in lines:
    the_sum = the_sum + int(line) 
    ##print(the_sum)

print(sum([int(x) for x in lines]))