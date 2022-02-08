a_dict = {"name":"keith", "address":"atlanta"} #{key}:value
a_dict['Phone'] = "401-212-9262"

#a_dict.update('phone' : '401-212-9262') #does not advocate that we use this
print(a_dict)

print(a_dict["name"])
a_var = "name"
print(a_dict[a_var])
print("name" in a_dict)
#a_list = [1,2,3]

#print(4 in a_list)

#print(a_dict.keys()) 
# or 
print(list(a_dict.keys()))
print(list(a_dict.values()))

print("keith" in list(a_dict.values()))

a_dict = {}
a_dict['key1']={}
a_dict['key2']={}
a_dict['key1']['values']=[]
a_dict['key1']['single_value'] = 3
a_dict['key1']['values'].append(4)
print(a_dict)
