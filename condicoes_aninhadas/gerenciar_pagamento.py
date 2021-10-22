class GerenciarPagamento:
    def __init__(self, preco, opcao):
        self.preco = preco
        self.opcao = opcao
        self.total = 0
        self.parcela = 0

    def calcularValor(self):
        if self.opcao == 1:
            self.total = self.preco - (self.preco * 10 / 100)

            print("sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(
                self.preco, self.total))
        elif self.opcao == 2:
            self.total = self.preco - (self.preco * 5 / 100)

            print("sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(
                  self.preco, self.total))
        elif self.opcao == 3:
            self.total = self.preco
            self.parcela = self.total / 2

            print("sua compra de R$ {:.2f} vai ser parcelada em 2x de R$ {:.2f}".format(
                self.total, self.parcela))
        elif self.opcao == 4:
            total_parcelas = int(input("quantas parcelas? "))
            self.total = self.preco + (self.preco * 20 / 100)
            self.parcela = self.total / total_parcelas

            print("sua compra de R$ {:.2f} vai ser parcelada em {}x de R$ {:.2f}".format(
                self.total, total_parcelas, self.parcela))
        else:
            print("ocorreu um erro tente novamente selecione as opções entre 1 a 4")


preco = float(input("valor da compra R$ "))
print('''
  [1] à vista dinheiro / cheque
  [2] à vista cartão
  [3] 2x no cartão
  [4] 3x ou mais no cartão
''')
opcao = int(input("qual é a opção? "))

gerenciarPagamento = GerenciarPagamento(preco, opcao)
gerenciarPagamento.calcularValor()
