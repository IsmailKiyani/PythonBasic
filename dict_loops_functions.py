students=("Ashraf","Hassan","Ahmed","Hamza")

print(type(students))

student_List=list(students)

print(type(student_List))

student_List[2]="Ahsan"

student_tuple=tuple(student_List)

print(type(student_tuple))

print(student_tuple)

"""Dictionary"""

employees={"Emp Code":25640,"Name":"Akram","Age":30, "Address":["Saddar","Johar"]}

print(type(employees))

print(employees["Age"])

check="Hamza" in student_List

print(check)

test_List=["Abc","Def"]

list_concat=student_List+test_List

print(list_concat)

finalList=test_List*2
print(finalList)

Cities=["Karachi","Lahore","Hyderabad"]
print(student_List)


for x in Cities:
  for y in student_List:
    print(x)

i=0
while i<3:
  i=i+1
  print(i)

if "Karachi" in Cities:
  if "Z" in Cities:
    print('Ok')
  else:
    print('N/A')
else:
  print('Not OK')

"""Functions"""

a=1
b=4
c=a+b
print(c)

#Non Parameterized
def AddFunc():
  a=1
  b=4
  return a+b

#Parameterized
def AddFuncWithParam(a,b):
  return a+b

#Without Return
def Hello():
  print("Hello K.E")

print(AddFunc())
print(AddFuncWithParam(b=5,a=5))

print(Hello())

print(AddFunc()+5)

print(AddFunc()-2)

def MyName(name='Ismail'):
  print("Hello !! I am "+name)


MyName(name='Hamza')

def square(a):
  return a*a

def applier(q,x):
  return q(x)

e=applier(square, 5)
print(e)

countries=["Pakistan","Turkey","Afghanistan","China","Italy"]
countries.pop()
countries[2]="Germany"
countries.insert(0,"Japan")
print(countries)