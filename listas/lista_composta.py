temp = []
lista = []

maior = menor = 0

while True:
    temp.append(str(input("digite um nome ")))
    temp.append(float(input("digite um peso ")))

    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()

    resposta = str(input("quer continuar? [S/N] "))

    if resposta in "Nn":
        break

print("-"*40)
print(f"foram cadastrados {len(lista)} pessoas")
print(f"o maior peso foi de {maior}kg ", end="")
for p in lista:
    if p[1] == maior:
        print(f"{p[0]} ", end="")

print(f"\no menor peso foi de {menor}kg ", end="")
for p in lista:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
