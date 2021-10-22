class ProgressaoAritimetica:
    def __init__(self, termo, razao):
        self.termo = termo
        self.razao = razao

    def contarPA(self):
        decimo = self.termo + (10 - 1) * self.razao
        contador = 0
        for c in range(termo, decimo + razao, razao):
            contador += 1
            print("{} ".format(c), end="-> ")
        print("acabou, a progresão tem {} numeros".format(contador))


termo = int(input("primeiro termo "))
razao = int(input("razão "))

progressaoAritimetica = ProgressaoAritimetica(termo, razao)
progressaoAritimetica.contarPA()
