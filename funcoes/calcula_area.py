class CalculaArea:
    def __init__(self, largura=0, comprimento=0):
        self.largura = largura
        self.comprimento = comprimento

    def area(self):
        return self.largura * self.comprimento


largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

calculaArea = CalculaArea(largura, comprimento)
print(calculaArea.area())
