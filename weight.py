weight = float(input("Какой у тебя вес?: "))

inches = input("(K)g или (L)bs: ").lower()
if inches == "k" or inches == "к":
    weight /= 0.45
    print("Твой вес " + str(weight) + " lbs")
elif inches == ("l"):
    weight *= 0.45
    print("Твой вес " + str(weight) + " kg")
else:
    print("Не пизди в единицах")