def aumentar(moeda=0, desconto=0):
    total = (desconto/100) * moeda
    return formatar_moeda(total + moeda)


def diminuir(moeda=0, desconto=0):
    total = (desconto/100) * moeda
    return formatar_moeda(moeda - total)


def dobro(moeda=0):
    return formatar_moeda(moeda * 2)


def metade(moeda=0):
    return formatar_moeda(moeda / 2)


def formatar_moeda(preco=0, moeda="R$ "):
    return f"{moeda}{preco:.2f}".replace(".", ",")
