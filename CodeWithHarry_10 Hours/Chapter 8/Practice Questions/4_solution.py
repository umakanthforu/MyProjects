# sum(n) = n + sum(n-1)
# factorial(n) = n * factorial(n-1)

def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)

print(sum(10))

# def factorial(m):
#     if(m==1 or m==0):
#         return 1
#     return m * factorial(m-1)

# print(factorial(10)) 