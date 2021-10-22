from datetime import datetime


class AlistamentoMilitar:
    def __init__(self, ano):
        self.ano = ano
        self.ano_atual = datetime.now().year
        self.idade = datetime.now().year - ano

    def alistar(self):
        if self.idade > 18:
            print("já passou o tempo de se alistar, voce esta atrasado {} ano(s)".format(
                self.ano_atual-self.ano))
        elif self.idade < 18:
            print("ainda não esta no tempo de se alistar falta {} ano(s)".format(
                self.ano_atual-self.ano))
        elif self.idade == 18:
            print("já esta no limite do tempo de se alistar")


ano = int(input("digite o ano em que nasceu "))

alistamento = AlistamentoMilitar(ano)

alistamento.alistar()
