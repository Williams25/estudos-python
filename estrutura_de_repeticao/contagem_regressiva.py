from time import sleep


class ContagemRegressiva:
    def __init__(self, numero=10):
        self.numero = numero

    def regressiva(self):
        for c in range(self.numero, 0, -1):
            sleep(1)
            print("{}".format(c))
        print("Fim")


contagemRegressiva = ContagemRegressiva(20)
contagemRegressiva.regressiva()
