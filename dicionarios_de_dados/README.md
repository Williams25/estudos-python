### Dicionários de dados

- `dicionario.py` Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

```py
aluno = {}

aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Media do {aluno['nome']}: "))

if aluno["media"] >= 6.5 and aluno["media"] <= 10:
    aluno["situacao"] = "aprovado"
elif aluno["media"] >= 6 and aluno["media"] < 6.5:
    aluno["situacao"] = "recuperação"
elif aluno["media"] <= 6 and aluno["media"] >= 0:
    aluno["situacao"] = "reprovado"
else:
    aluno["situacao"] = "inválida"

print(f"O aluno {aluno['nome']} teve sua média {aluno['media']} e sua situação é {aluno['situacao']}")
```

- `jogo_dados.py` Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

```py
from random import randint
from time import sleep
from operator import itemgetter

ranking = []
dado = {}

dado["jogador1"] = randint(1, 6)
dado["jogador2"] = randint(1, 6)
dado["jogador3"] = randint(1, 6)
dado["jogador4"] = randint(1, 6)

print("Valores sorteados:")

for key, value in dado.items():
    print(f" {key} tirou {value} no dado.")
    sleep(1)

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

print("\nRanking:")

for index, value in enumerate(ranking):
    print(f" {index+1} lugar: {value[0]} com {value[1]}")
    sleep(1)
```

- `cadastro_trabalhador.py` Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

```py
from datetime import datetime

cadastro = {}

cadastro["nome"] = str(input("Nome: "))
cadastro["ano_nascimento"] = int(input("Ano de nascimento: "))
cadastro["idade"] = datetime.now().year - cadastro["ano_nascimento"]
cadastro["ctps"] = int(input("Carteira de trabalho (0 não tem): "))

if cadastro["ctps"] != 0:
    cadastro["ano_contratacao"] = int(input("Ano de contratação: "))
    cadastro["salario"] = float(input("Salario R$: "))
    cadastro["aposentadoria"] = cadastro["idade"] + \
        ((cadastro["ano_contratacao"] + 35) - datetime.now().year)

    print(
        f"O trabalhador {cadastro['nome']} tem {cadastro['idade']}", end=" ")
    print(f"anos sua carteira de trabalho é {cadastro['ctps']}", end=" ")
    print(
        f"e seu salario é de {cadastro['salario']} e vai se aposentar com {cadastro['aposentadoria']} anos")
```

- `cadastro_jogador_futebol.py` Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
  - Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

```py
jogadores = []
gols = []
dados = {}

while True:
    gols.clear()
    dados.clear()

    dados["nome"] = str(input("Nome: "))
    dados["partidas"] = int(
        input(f"Quantas partidas o jogador {dados['nome']} jogou? "))

    for i in range(0, dados["partidas"]):
        gols.append(int(input(f"Gols na partida {i+1}: ")))

    dados["gols"] = gols[:]
    dados["total_gols"] = sum(gols)

    jogadores.append(dados.copy())

    while True:
        resposta = str(input("quer continuar? [S/N] "))
        if resposta in "NnSs":
            break
        print("Erro digite apenas S ou N")
    if resposta in "Nn":
        break


print(jogadores)

print('-='*30)
print(f"{'Cod.':<4} {'Nome':<8} {'Gols':^8} {'total':>8}")
print('-='*30)

for index, value in enumerate(jogadores):
    print(
        f"{index:<4} {jogadores[index]['nome']:<8} {jogadores[index]['gols']} {jogadores[index]['total_gols']:>8}")
print('-='*30)

while True:
    index = int(
        input("Qual jogador que ver os detalhes? [999 para parar] "))

    if index == 999:
        break
    elif index != 999 and index > len(jogadores)-1:
        print("Erro digite um valor valido")
    else:
        for i, value in enumerate(jogadores[index]['gols']):
            print(f" No jogo {i+1} o jogador {jogadores[index]['nome']} fez {value} gols")
```

- `dicionarios_e_listas.py` Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
  - Quantas pessoas foram cadastradas
  - A média de idade
  - Uma lista com as mulheres
  - Uma lista de pessoas com idade acima da média

```py
dados = {}
lista = []
mulheres = []
acima_media = []
media = 0

while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    dados["idade"] = int(input("Idade: "))

    while True:
        dados["sexo"] = str(input("Sexo [M/F]: "))
        if dados["sexo"] in "MmFf":
            break
        print("Erro digite apenas M ou F")

    lista.append(dados.copy())

    while True:
        resposta = str(input("quer continuar? [S/N] "))
        if resposta in "NnSs":
            break
        print("Erro digite apenas S ou N")

    if resposta in "Nn":
        break

for index, value in enumerate(lista):
    media += lista[index]['idade']

media = media / len(lista)

for index, value in enumerate(lista):
    if lista[index]['sexo'] in "Ff":
        mulheres.append(lista[index])
    if lista[index]['idade'] > media:
        acima_media.append(lista[index])

print(f" - foram cadastradas {len(lista)} pessoas")
print(f" - a media de idade é {media:0.0f} anos")

if len(mulheres) > 0:
    print(f"\n - lista de mulheres")
    for index, value in enumerate(mulheres):
        print(f"  - {mulheres[index]['nome'].upper()}")

if len(acima_media) > 0:
    print(f"\n - lista de pessoas com idade acima da media:")
    for index, value in enumerate(acima_media):
        print(
            f"  - {acima_media[index]['nome'].upper()} {acima_media[index]['idade']} anos sexo {acima_media[index]['sexo'].upper()}")
```
