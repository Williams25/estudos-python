class Media:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0

    def calcular(self):
        self.media = (self.nota1 + self.nota2) / 2

        if self.media >= 7.0 and self.media <= 10.0:
            print("aprovado sua media é {}".format(self.media))
        elif self.media >= 5.0 and self.media <= 6.9:
            print("recuperação sua media é {}".format(self.media))
        elif self.media < 5.0:
            print("reprovado sua media é {}".format(self.media))
        else:
            print("ocorreu um erro ao calcular sua media")


nota1 = int(input("digite a primeira nota "))
nota2 = int(input("digite a segunda nota "))

media = Media(nota1, nota2)
media.calcular()
