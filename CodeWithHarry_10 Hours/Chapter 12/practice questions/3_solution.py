# num = int(input("Enter the number :"))
#-------------------------------------------------------------------
### using for loop
# for i in range (1,11):
#     print(f"{num} X {i} = {num*i}\n")
#-------------------------------------------------------------------
### using while loop

# i=1
# while i<=10:
#     print(f"{num} X {i} = {num*i}\n")
#     i +=1

#--------------------------------------------------------------------
# writing tables in to files

# for i in range (1,21):
#     table =''
#     for j in range(1,11):
#         table += f"{i} X {j} = {j*i}\n"
#         with open(f'tables/{i}.txt', 'w') as f:
#             f.write(table)
#-------------------------------------------------------------------

num = int(input("Enter the number desired for table"))

multiplication = [i*num for i in range(1, 11)]
print(multiplication)