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
