from random import randint


class SortearSomar:
    def __init__(self):
        self.lista = []
        self.total_par = 0

    def sortear(self):
        print(f"os numeros sorteados foram:")
        for i in range(0, 5):
            self.lista.append(randint(1, 50))
        print(self.lista)

    def somaPar(self, lista=[]):
        print(f"os numeros pares sorteados foram:")
        for i in lista:
            if i % 2 == 0:
                print(f"{i}", end=" ")
                self.total_par += i

        print(f"\na soma dos numeros pares sorteados foram {self.total_par}")


sortear_somar = SortearSomar()
sortear_somar.sortear()
sortear_somar.somaPar(sortear_somar.lista)
