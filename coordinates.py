numbers = [2,4,9,4,8,3,2]
output = ""
for number in numbers:
    for y in range(number):
        output += "*"
    print(output)
    output = ""

biggest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
print(biggest)