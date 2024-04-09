lambda x:x+1

x=lambda y:y+10

print(x)

print(x(5))

a=lambda b :b*2

print(a(5))

a=lambda x,y,z: x+y * (z - 2)

print(a(2,5,4))

c=5
def add():
  a=1
  b=2
  return a+b+c

def mul(b):
  return b*a

print(" Value of C is :",c)
print("\n Addition is : ",add())
print("Multiplication is : \t",mul(2))

import operator

def addor(x):
  return x+5

list_test=[5,6,9,2]

q=map(addor, list_test)
print(list(q))

def func(x):
  if x>=5:
    return x
n=filter(func,(1,2,3,4,5,6,7))
print(n)

print(list(n))

from functools import reduce

values=[10,5,20,3,2,10]

totalvalues=reduce(lambda a,b:a+b,values)

print(totalvalues)

X=input("Enter your number : ")

print(X)