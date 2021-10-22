class Palindromo:
    def __init__(self, frase=""):
        self.frase = frase.strip().upper()
        self.palavras = self.frase.split()
        self.palavra = "".join(self.palavras)
        self.palavra_inversa = ""

    def palindromo(self):
        for letra in range(len(self.palavra) - 1, -1, -1):
            self.palavra_inversa += self.palavra[letra]
        if (self.palavra_inversa == self.palavra):
            print("A palavra {} é um palindrome, ela invertida fica {}".format(
                self.palavra, self.palavra_inversa))
        else:
            print("A palavra {} não é um palindrome, ela invertida fica {}".format(
                self.palavra, self.palavra_inversa))


palindromo = Palindromo("o lobo ama bolo")
palindromo.palindromo()
