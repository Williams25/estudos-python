class SomaImpares:
    def __init__(self, numero=500):
        self.numero = numero

    def soma(self):
        acumulador = 0
        contador = 0
        for c in range(1, self.numero + 1, 2):
            if c % 3 == 0:
                acumulador = acumulador + c
                contador += 1
                print("o numero {} é multiplo pro 3".format(c))

        print("a soma dos valores multiplos por 3 é {}".format(acumulador))
        print("foram encontrados {} numeros multiplos por 3".format(contador))


somaImpares = SomaImpares(10)
somaImpares.soma()
