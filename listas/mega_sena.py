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
