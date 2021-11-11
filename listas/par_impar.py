numeros = [[], []]

for i in range(0, 7):
    num = int(input("digite um numero "))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f"os numeros pares foram {numeros[0]}")
print(f"os numeros impares foram {numeros[1]}")
