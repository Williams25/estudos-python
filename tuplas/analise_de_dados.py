numeros = (int(input("Digite um numero: ")), int(input("Digite um numero: ")), int(
    input("Digite um numero: ")), int(input("Digite um numero: ")))

position3 = ""

print("os numeros pares são: ", end="")

for i in numeros:
    if i % 2 == 0:
        print("{} ".format(i), end="")

print("\no numero 9 apareceu {}x".format(numeros.count(9)))
if 3 in numeros:
    print("o numero 3 esta na {}° posição".format(numeros.index(3)+1))
else:
    print("o numero 3 não esta em nenhuma posição")
