lista = []
pares = []
impares = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    lista.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if resposta in "Nn":
        break

print(f"Lista {lista}")
print(f"Numeros pares {pares}")
print(f"Numeros impares {impares}")
