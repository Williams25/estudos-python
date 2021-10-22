class SomaPares:
    def __init__(self, numero):
        self.numero = numero

    def soma(self):
        acumulador = 0
        contador = 0
        for c in range(1, self.numero + 1):
            if c % 2 == 0:
                acumulador = acumulador + c
                contador += 1
                print("o numero {} é par".format(c))

        print("a soma dos valores pares é {}".format(acumulador))
        print("foram encontrados {} numeros pares".format(contador))


somaPares = SomaPares(10)
somaPares.soma()
