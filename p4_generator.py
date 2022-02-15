import random


frequencies = []

f=open("p4.txt","w")
for i in range(0,100000):
    #pick a random sensor
    freq = random.randint(-999,999)
    #frequencies.append(freq)
    f.write(f"{freq}\n")


