teams=('England','India','New Zealand','Pakistan')
print(teams)

print(type(teams))

print(teams[1:3])

list_teams=list(teams)

print(type(list_teams))

list_teams[1]='Bangladesh'

print(list_teams)
teams=tuple(list_teams)
print(type(teams))
print(teams)

teams1=('Australia','Zimbabwe')

teams+=teams1

print(teams)

teams2=('England','Pakistan')
print(teams2)

(T1,T2)=teams2

print(T1)
print(T2)
print(type(T1))