class MaiorMenorSequencia:
    def __init__(self, pesos):
        self.pesos = pesos
        self.menor_peso = 0
        self.maior_peso = 0

    def sequencia(self):
        index = 0
        for peso in self.pesos:
            if index == 0:
                self.menor_peso = peso
                self.maior_peso = peso
            else:
                if peso > self.maior_peso:
                    self.maior_peso = peso
                elif peso < self.menor_peso:
                    self.menor_peso = peso
            index += 1

        print("o maior peso lido foi de {}kg".format(self.maior_peso))
        print("o menor peso lido foi de {}kg".format(self.menor_peso))


pesos = [40.0, 5.20, 60.95, 90.95, 75.52]

maiorMenorSequencia = MaiorMenorSequencia(pesos)
maiorMenorSequencia.sequencia()
