### Tuplas

- `times.py` Crie uma tupla preenchida com os da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

  - Os 5 primeiros times.
  - Os últimos 4 colocados.
  - Times em ordem alfabética.
  - Em que posição está o time da Corinthians.

```py
times = ("corinthians", "palmeiras", "santos", "gremio", "cruzeiro",
         "coritiba", "flamengo", "ponte preta", "atletico-go", "atletico-mg")

print(times)
print(times[:5])
print(times[6:])
print(sorted(times))
print(times.index("corinthians") + 1)
```

- `maior_menor.py` Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

```py
from random import randint

n = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))

maior = 0
menor = 0

for i in range(0, len(n)):
    if i == 0:
        maior = n[i]
        menor = n[i]
    else:
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]
print(n)
print("o maior numero sorteado foi {}".format(maior))
print("o menor numero sorteado foi {}".format(menor))
```

- `analise_de_dados.py` Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

  - Quantas vezes apareceu o valor 9.
  - Em que posição foi digitado o primeiro valor 3.
  - Quais foram os números pares.

```py
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
```

- `lista_de_preco` Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

```py
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
```

- `vogais.py` Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

```py
palavras = (
    "aprender",
    "programar",
    "estudar",
    "linguagem",
    "python",
    "trabalhar",
    "mercado"
)

for p in palavras:
    print("\nna palavra {} temos as seguintes vogais ".format(p.upper()), end="")

    for letra in p:
        if letra.lower() in "aeiou":
            print("{}".format(letra), end=" ")
```
