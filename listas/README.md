### Funções

### Listas

- `numero_por_extenso.py` Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

```py
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
```

- `valores_unicos.py` Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

```py
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
```

- `lista_ordenada.py` Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

```py
lista = []

for i in range(0, 5):
    num = int(input("digite um numero "))

    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print("-"*30)
print(f"lista ordenada {lista}")
print("-"*30)
```

- `extraindo_dados.py` Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
  - Quantos números foram digitados.
  - A lista de valores, ordenada de forma decrescente.
  - Se o valor 5 foi digitado e está ou não na lista.

```py
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
```

- `multiplas_listas.py` Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

```py
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
```

- `validando_expressoes.py` Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

```py
expr = str(input("digite uma espressao "))

pilha = []

for simbolo in expr:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("expressao correta")
else:
    print("expressao incorreta")
```

- `lista_composta.py` Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
  - Quantas pessoas foram cadastradas.
  - Uma listagem com as pessoas mais pesadas.
  - Uma listagem com as pessoas mais leves.

```py
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
```

- `par_impar.py` Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

```py
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
```

- `matriz.py` Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. mostre:
  - A soma de todos os valores pares digitados.
  - A soma dos valores da terceira coluna.
  - O maior valor da segunda linha.

```py
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
```

- `mega_sena.py` Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

```py
from random import randint
from time import sleep

lista = []
jogos = []
total = 1
quantidade = int(input("quantos jogos serão gerados? "))

while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("-="*3, f" SORTEANDO {quantidade} JOGOS ", "=-"*3)

for index, valor in enumerate(jogos):
    print(f"Jogo {index+1}: {jogos[index]}")
    sleep(1)

print("-="*5, f" BOA SORTE ", "=-"*5)
```

- `boletim.py` Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

```py
lista = []
alunos = []

while True:
    lista.append(str(input("nome: ")))
    lista.append(float(input("nota 1: ")))
    lista.append(float(input("nota 2: ")))
    resposta = str(input("quer continuar? [S/N] "))

    alunos.append(lista[:])
    lista.clear()

    if resposta in "Nn":
        break

print('-'*26)
print(f"{'No.':<4}{'Nome':<10}{'Media':>8}")
print('-'*26)

for index, valor in enumerate(alunos):
    alunos[index].append((alunos[index][1] + alunos[index][2]) / 2)
    print(f"{index:<4}{valor[0]:<10}{valor[3]:>8.1f}")

print('-'*26)

while True:
    opcao = int(input("mostrar notas de qual aluno? (999 interromper)"))
    if opcao == 999:
        break
    if opcao <= len(alunos) - 1:
        print(f"Nota 1: {alunos[opcao][1]}, Nota 2: {alunos[opcao][2]}")
    else:
        print("opcao incorreta")
```
