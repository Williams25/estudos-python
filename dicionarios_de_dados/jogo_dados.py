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
