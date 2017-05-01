import random

for i in range(random.randrange(1,101)):
	people = ["John","Nick","Ben","Jeremy","Eric"]
	random.shuffle(people)
selected = random.randrange(0,5)

print(people[selected])