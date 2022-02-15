a_list = [0,13,95,34,56,12]
#print(a_list[0])
#print(a_list[-1]) #last element = -1

#print(a_list[0:3]) #print element 0, 1 and 2
#print(a_list[-3:-1])
#print(a_list[3:]) #3rd element to end

#print(a_list[1::2]) #start at 1 skip every other
#print(a_list[3::-1]) #reverse list from 3
#print(a_list[::-1]) 
#a_list = list(reversed(a_list)) #reversed
a_list.reverse() #also reverse
print(a_list)

a_list.sort() #in place 
print(a_list)

print(sorted(a_list)) #sorts from low to high

a_list.append(7) #adds 7 to end of list

print(a_list)

a_list.extend([53,27]) #adds 52 and 27 to list

print(a_list)

a_list.append([342,234]) #adds string within string
print(a_list)

a_list.pop()

print(a_list)

a_list.remove(95) #removes specific value
print(a_list)

del a_list[3] #removes 3rd (4th) in list object
print(a_list)

a_list = a_list[0:3] #removes all but first 3 elements

print(a_list)

#a_list.insert(0,3) #adds 3 to front of list
#print(a_list)

a_list.insert(2,3) #adds 3 at 2 place
print(a_list)

del a_list[0:3]
print(a_list)

#finding the deltas for an integer list
a_list = [3,5,7,10,1,6]

for second_num in a_list[1::2]: #prints every other number
    print(second_num)

deltas = []
for i in range(1,len(a_list)):
    deltas.append(a_list[i] - a_list[i-1])
print(deltas)

