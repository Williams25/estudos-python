class NumerosPrimos:
    def __init__(self, numero=0):
        self.numero = numero

    def primos(self):
        total = 0
        for c in range(1, self.numero+1):
            numero_primo = self.numero % c
            if numero_primo == 0:
                total += 1
                print("\033[33m", end=' ')
            else:
                print("\033[31m", end=' ')
            print("{}".format(c), end=' ')

        if total == 2:
            print("\n\033[mo numero {} é primo ele foi dividido {}x".format(
                self.numero, total))
        else:
            print("\n\033[mo numero {} não é primo".format(self.numero))


numerosPrimos = NumerosPrimos(7)
numerosPrimos.primos()
