class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


lit = []
obj = []


b = 1

while True:
	z = input("do what ")

	if z.lower() == "input":
		lit.append(input(f"object name {b} "))
		b = b+1
	else:
		break

print(lit)

for j in range(len(lit)):
    namez = input("name ")
    agez = input("age ")
    obj.append(Person(namez, agez))

for i in range(len(lit)):
    print(str(i) + ":", lit[i], end=" ")

a = int(input("which item "))
print(obj[a].name)
print(obj[a].age)
