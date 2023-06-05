dict = {
    ":)": "хер",
    ":(": "хрен"
}

phrase = input("> ")
words = phrase.split(" ")

result = ""
for word in words:
    result += dict.get(word, word) + " "

print(result)