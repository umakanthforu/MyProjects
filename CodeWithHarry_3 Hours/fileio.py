s = "Umakanth is a good programmer"

# writing a file 

# EASY WAY

# # with open("test.txt", "w") as f:
# #     f.write(s)

# DIFFICULT WAY

# fp = open("text.txt", "w")
# fp.write(s)
# fp.close()

# READING A FILE

# EASY WAY

# with open("text.txt", "r") as f:
#     s = f.read()
#     print(s)

# DIFFICULT WAY

fp = open("text.txt", "r")
read = fp.read()
print(read)
fp.close() 