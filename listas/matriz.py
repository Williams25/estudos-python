matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"digite um numero para [{l}, {c}]: "))

print("*"*30)

impares = pares = maior_valor_segunda_linha = soma_terceira_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        else:
            impares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[l][c]
    print()

print(f"a soma dos valores pares são {pares} e impares são {impares}")
print(f"a soma dos valores da terceira coluna é de {soma_terceira_coluna}")
print(f"o maior valor da segunda linha é de {maior_valor_segunda_linha}")
