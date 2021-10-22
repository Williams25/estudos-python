class Conversao:
    def __init__(self, num, opcao):
        self.num = num
        self.opcao = opcao

    def conversao(self):
        if opcao == 1:
            print("{} convertido para binário é igual a {}".format(
                self.num, bin(self.num)[2:]))
        elif opcao == 2:
            print("{} convertido para octal é igual a {}".format(
                  self.num, oct(self.num)[2:]))
        elif opcao == 3:
            print("{} convertido para hexadecimal é igual a {}".format(
                  self.num, hex(self.num)[2:]))
        else:
            print("opção {} inválida".format(
                  self.opcao))


num = int(input("digite um numero "))
opcao = int(input('''
  [1] converter para binário
  [2] converter para octal
  [3] converter para hexadecimal
'''))

conversor = Conversao(num, opcao)
conversor.conversao()
