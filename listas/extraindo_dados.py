lista = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    lista.append(num)

    if resposta in "Nn":
        break

lista.sort(reverse=True)

print("foram digitados {} numeros ".format(len(lista)))
print(lista)

if 5 not in lista:
    print("o numero 5 não foi encontrado")
else:
    print("o numero 5 foi encontrado")
