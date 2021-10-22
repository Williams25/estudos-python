from random import randint
from time import sleep


class Jokenpo:
    def __init__(self, opcao=1):
        self.itens = ("Pedra", "Papel", "Tesoura")
        self.random = randint(0, 2)
        self.opcao = opcao - 1  # 1,2,3

    def jogar(self):
        if self.opcao >= 0 and self.opcao <= 2:
            self.start()
            print("-=" * 11)
            print("Computador jogou {}".format(self.itens[self.random]))
            print("Voce jogou {}".format(self.itens[self.opcao]))
            print("-=" * 11)

            if self.opcao == self.random:
                print("{} Empate {}".format('💢'*11, '💢'*11))
            elif self.opcao == 0 and self.random == 1:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            elif self.opcao == 0 and self.random == 2:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 1 and self.random == 0:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 1 and self.random == 2:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            elif self.opcao == 2 and self.random == 1:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 2 and self.random == 0:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            else:
                print("ocorreu um erro inesperado, tente novamente")
        else:
            print("Opção invalida jogue novamente e escolha entre 1 e 3")

    def start(self):
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)


print('''
  [1] Pedra
  [2] Papel
  [3] Tesoura
''')

opcao = int(input("Qual a sua jogada? "))

jokenpo = Jokenpo(opcao)
jokenpo.jogar()
