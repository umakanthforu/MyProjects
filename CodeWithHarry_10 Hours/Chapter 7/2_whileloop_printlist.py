## PRINTING CONTENT OF LIST USING WHILE LOOP ###

list = [12, 4, 23, 345, 654]

list.append("banana")
print(list)
print(len(list))
print(list[5])

i=0
while i<len(list):
    print(list[i])
    i +=1