class ContagemPares:
    def __init__(self, numero=50):
        self.numero = numero

    def contagem(self):
        for c in range(0, self.numero + 1):
            if c % 2 == 0:
                print("o numero {} é par".format(c))


contagemPares = ContagemPares(10)
contagemPares.contagem()
