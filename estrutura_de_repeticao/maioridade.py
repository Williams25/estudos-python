from datetime import datetime


class Maioridade:
    def __init__(self, ano_nascimento=[]):
        self.ano_nascimento = ano_nascimento

    def maioridade(self):
        maior = 0
        menor = 0

        for ano in self.ano_nascimento:
            ano_atual = datetime.now()
            idade = ano_atual.year - ano

            if idade >= 21:
                maior += 1
            elif idade < 18:
                menor += 1

        print("{} pessoas atigiram a maioridade".format(maior))
        print("{} pessoas não atigiram a maioridade".format(menor))


anos = [1975, 2000, 2002, 2003, 2004, 2005, 2006, 1999, 1990, 1998]
maioridade = Maioridade(anos)

maioridade.maioridade()
