lista = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    if num not in lista:
        lista.append(num)
    else:
        print("valor duplicado")
    if resposta in "Nn":
        break

lista.sort()
print(lista)
