lista = ("lapis", 1.75, "borracha", 2.00, "estojo", 25.00, "caderno", 15.00)

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end="")
    else:
        print(f" R$ {lista[i]:>5.2f}")

print("-"*40)
