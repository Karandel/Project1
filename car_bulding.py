possible_cmd = ["Start","Stop","Quit"]
qflag = False
carstate = "stopped"

while qflag != True:
    print("Введи команду для своей тачки:")
    for pc in possible_cmd:
        print("* " + pc)

    command = input("> ")

    if command.capitalize() not in possible_cmd:
        print("Ну ты и балбес...")
        continue

    if command.capitalize() == "Start":
        if carstate == "started":
            print("Ты уже едешь")
            continue
        else:
            print("Твоя тачка поехала")
            carstate = "started"
            continue
    elif command.capitalize() == "Stop":
            if carstate == "stopped":
                print("Ты уже стоишь")
            else:
                print("Твоя тачка остановилась")
                carstate = "stopped"
                continue
    else:
        print("Выход")
        qflag = True
