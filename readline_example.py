file_handle=open('test.txt')
lines = file_handle.readlines()
print(lines)
file_handle.close()


file_handle=open('test.txt')
lines = [ x.strip() for x in file_handle.readlines()]
print(lines)
file_handle.close()

file_handle=open('test.txt')
file_data = file_handle.read()
file_lines = file_data.split("\n")#strips \n
print(file_lines)
file_handle.close()

file_handle=open('test.txt')
file_lines = []
while True:
    line = file_handle.readline()
    if line == "": 
        break
    file_lines.append(line.strip()) #print adds new line
print(file_lines)
file_handle.close()

