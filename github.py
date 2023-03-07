# Too lazy for now to make separate files interact between each other, so only 1 file
print("Настоящий пароль:")
truepass = str(input())
while truepass == "12345678":
    print("Пароль слишком слабый, введите другой")
    truepass = str(input())
else:
    print("Пароль:")
    passtry = str(input())
    while passtry != truepass:
        print("Неверный пароль, попробуйте снова")
        passtry = str(input())
    else:
        if passtry == truepass:
            print("Пароль верный")
        else:
            print("no hax")