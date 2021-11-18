def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(msg))

        if valor.isalpha() or len(valor.strip()) == 0:
            print(f"\033[0;31mDigite um valor valido!\033[m")
        else:
            valido = True
            return float(valor.replace(",", "."))
