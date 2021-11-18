def aumentar(moeda=0, desconto=0, formatar=False):
    total = (desconto/100) * moeda
    if formatar:
        return formatar_moeda(total + moeda)
    return total + moeda


def diminuir(moeda=0, desconto=0, formatar=False):
    total = (desconto/100) * moeda
    if formatar:
        return formatar_moeda(moeda - total)
    return moeda - total


def dobro(moeda=0, formatar=False):
    if formatar:
        return formatar_moeda(moeda * 2)
    return moeda * 2


def metade(moeda=0, formatar=False):
    if formatar:
        return formatar_moeda(moeda / 2)
    return moeda / 2


def formatar_moeda(preco=0, moeda="R$ "):
    return f"{moeda}{preco:.2f}".replace(".", ",")
