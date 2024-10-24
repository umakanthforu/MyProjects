# myset = {2, 3, 5}
# # print(myset)
# # # for a in myset:
# # #     print(a)

# # myset.add(99) # to add any element
# # print(myset)

# # print(len(myset)) # to print length of set

# # myset.remove(99) # to remove element from set

# # print(myset)
# # print(len(myset))

# # myset.pop() # to remove random element from set
# # print(myset)
# # print(len(myset))

# # myset.pop()
# # print(myset)
# # print(len(myset))

# sunset = {1, 2, 3, 4}
# print(sunset)


# for a in sunset:
#     print(a)

# sunset.add("umakanth")
# sunset.add(12)
# sunset.remove(1)

# print(sunset)
# print(len(sunset))
# sunset.clear()
# print(sunset)


a = {1, 2, 4, 5}
b = {2, 3, 6}

print(a.union(b)) # prints union
print(a.intersection(b)) # prints common elements

print(a.intersection({2, 3, 4})) # prints with intersection of elements passed

print(a.union({9, 11})) # prints with union of elements passed