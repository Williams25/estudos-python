class ComparandoNumeros:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def comparando(self):
        if self.num1 > self.num2:
            print("o primeiro numero {} é maior que o segundo numero {}". format(
                self.num1, self.num2))
        elif self.num1 < self.num2:
            print("o segundo numero {} é maior que o primeiro numero {}". format(
                self.num2, self.num1))
        elif self.num1 == self.num2:
            print("o primeiro numero {} é igual o segundo numero {}". format(
                self.num1, self.num2))
        else:
            print("aconteceu algo inesperado")


num1 = int(input("digite um numero "))
num2 = int(input("digite um numero "))

comparandoNumeros = ComparandoNumeros(num1, num2)
comparandoNumeros.comparando()
