lista = []

maior = 0
menor = 0

for index in range(0, 5):
    lista.append(
        int(input(f"Digite um numero na posicao {index}: "))
    )
    if index == 0:
        maior = lista[index]
        menor = lista[index]
    else:
        if lista[index] > maior:
            maior = lista[index]
        if lista[index] < menor:
            menor = lista[index]

print("-"*40)
print(lista)
print("-"*40)
print(f"o maior valor encontrado foi {maior} na posicao ", end=" ")

for index, valor in enumerate(lista):
    if lista[index] == maior:
        print(f"{index}", end=" ")

print(f"\no menor valor encontrado foi {menor} na posicao ", end=" ")

for index, valor in enumerate(lista):
    if lista[index] == menor:
        print(f"{index}", end=" ")
