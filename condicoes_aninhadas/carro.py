class Carro:
    def __init__(self, direcao="siga"):
        self.direcao = direcao

    def siga(self):
        if self.direcao == 'siga':
            return True

    def direita(self):
        if self.direcao == 'direita':
            return True

    def esquerda(self):
        if self.direcao == 'esquerda':
            return True

    def dirigir(self):
        if (self.siga()):
            print("siga")
        elif (self.esquerda()):
            print("esquerda")
        elif (self.direita()):
            print("direita")
        else:
            print("ré")


carro = Carro("esquerda")
carro.dirigir()
