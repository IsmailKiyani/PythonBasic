teams={"Germany","France","Uruguay"}

print(teams)

print(type(teams))

print(len(teams))


for x in teams:
    print(x)

a="Pakistan" in teams
print(a)

teams.add("Pakistan")
print(teams)

teams1={"Pakistan","India"}

teams.update(teams1)
print(teams)


sameValue = teams.intersection(teams1)
print(sameValue)

teams.symmetric_difference_update(teams1)
print(teams)

teams.remove("India")
print(teams)

teams.discard("Poland")
print(teams)

teams.pop()
print(teams)