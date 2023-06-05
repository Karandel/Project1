numbers = [1,5,23,78,3,3]

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)