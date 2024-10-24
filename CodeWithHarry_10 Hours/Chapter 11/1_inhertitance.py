class A:
    a = 25

class B(A):
    b = 50

cl = B()
print(cl.b)
print(cl.a)

cla = A()
print(cla.a)
print(cla.b) # It throws error as B has inherited A but A has not inherited B