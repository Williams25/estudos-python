def leiaInt():
    while True:
        value = input("Digite um numero: ")
        if value.isnumeric():
            break
        else:
            print("Somente numeros são validos")


leiaInt()
