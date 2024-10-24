# list = [1, 2, 3, 4, 5, 6]

# item=0
# for item in range(len(list)):
#     print(list[item])
#     if(item==3):
#         break # it breaks the loop here and exits
#     print("Iteration completed", item)
    
# print("DOne")

#####CONTINUE#############
list = [1, 2, 3, 4, 5, 6]

item=0
for item in range(len(list)):
    print(list[item])
    if(item==3):
        continue # it continues  the loop here and exits
    print("Iteration completed", item)
    
print("DOne")