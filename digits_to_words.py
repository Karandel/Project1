dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

digits = input("Напиши свои цифры: ")

result = ""
for digit in digits:
    result += dict.get(digit) + " "

print(result)