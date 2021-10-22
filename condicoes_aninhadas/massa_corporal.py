class MassaCorporal:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.massa = 0

    def imc(self):
        self.massa = self.peso / (self.altura**2)

        if self.massa < 18.5:
            print("abaixo do peso, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 18.5 and self.massa <= 25:
            print("peso ideal, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 25 and self.massa <= 30:
            print(
                "esta em sobrepeso, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 30 and self.massa <= 40:
            print(
                "esta em obesidade, sua massa é de {:.1f}". format(self.massa))
        else:
            print(
                "esta em obesidade morbida, sua massa é de {:.1f}". format(self.massa))


peso = float(input("qual seu peso? "))
altura = float(input("qual sua altura? "))

massaCorporal = MassaCorporal(peso, altura)
massaCorporal.imc()
