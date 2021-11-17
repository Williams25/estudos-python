from datetime import datetime


class Eleicao:
    def __init__(self):
        self.ano_atual = datetime.now().year

    def voto(self, ano=1910):
        idade = self.ano_atual - ano

        if idade >= 16 and idade < 18 or idade >= 65:
            return "OPCIONAL"
        elif idade < 16:
            return "NEGADO"
        elif idade > 18 and idade <= 64:
            return "OBRIGATÓRIO"


print(Eleicao().voto(1999))
