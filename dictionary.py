Student={'Name':'Haider','Age':30,'Class':'Python'}

print(Student)
print(type(Student))
print(Student["Age"])

print(Student['Class'])
print(Student.get('Name'))

print(Student.keys())

print(Student.values())

Student["Year"]=2022
print(Student)

Student['Age']=40
print(Student)

Student.update({'Year':2020})
print(Student)

Student.pop('Year')
print(Student)

Student.popitem()
print(Student)

del Student

Class1={'Subject':'Python','Strength':30}
Class2={'Subject':'English','Strength':20}
Class3=['Subject','Strength']

Semester={'First':Class1,'Second':Class2,'Third':Class3}
print(Semester)

Student={'Name':'Haider','Age':30,'Class':'Python'}

for x,y in Student.items():
  print(x,y)

lst_city=['Karachi','Lahore','Hunza']

z='Quetta' in lst_city
print(z)