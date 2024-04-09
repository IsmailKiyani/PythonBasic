"""**List**"""

teams=["Pakistan","India","Australia","England"]
print(teams)

print(len(teams))

print(teams[0])

print(teams[-1])

print(teams[:2])

teams[0]='Africa'

print(teams)

teams[1:3]=["Pakistan","Ireland"]
print(teams)

teams[2:4] = ["India"]
print(teams)

teams.insert(2, "Sri Lanka")
print(teams)

teams.append("Zimbabwe")
print(teams)

teams1=["Australia","India","Ireland"]
teams.extend(teams1)
print(teams)

# Remove By Value  "India"
# Pop By Index    3

teams.remove("Pakistan")
print(teams)

teams.pop(1)
print(teams)

teams.pop()
print(teams)

teams.clear()
print(teams)

del teams
print(teams)