text = input("Придумай предложение со словом хер: ")
if ("хер" in text) == True:
    print(text.replace("хер", "член"))
else:
    print("Но ты не упомянул слово хер...")