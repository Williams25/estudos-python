def aumentar(moeda, desconto=10):
    total = (desconto/100) * moeda
    return total + moeda


def diminuir(moeda, desconto=10):
    total = (desconto/100) * moeda
    return moeda - total


def dobro(moeda):
    return moeda * 2


def metade(moeda):
    return moeda / 2
