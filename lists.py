names = ["Серж", "Олежек", "Антошка", "Димасик"]
names.append("Костянчик")
print(names[-1])
print("Серж" in names)
print(len(names))

i = 0

while i <= len(names)-1:
    print(names[i])
    i += 1

for item in names:
    print(item)

numbers = range(0, 5, 3)
for number in numbers:
    print(number)