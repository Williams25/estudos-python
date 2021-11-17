from time import sleep


class Contador:
    def __init__(self, inicio=10, fim=0, passo=1):
        self.inicio = inicio
        self.fim = fim
        self.passo = passo

    def contador(self):
        print("-="*30)
        print(f"Contagem de 1 até 10, de 1 em 1")
        for i in range(1, 11):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)

        print("-="*30)
        print(f"Contagem de 10 até 0, de 2 em 2")
        for i in range(10, 0, -2):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)

        print("-="*30)
        print(
            f"Contagem personalizada inicio {self.inicio} fim {self.fim} e pula de {self.passo} em {self.passo}")
        for i in range(self.inicio, self.fim, self.passo):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)


inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

Contador(inicio, fim, passo).contador()
