secret = "9"

for i in range(0,3):
    print("Попытка номер " + str(i + 1))
    answer = input("Угадай число: ")
    if answer == secret:
        print("Ты победил!")
        break
    else:
        print("Лузер")
