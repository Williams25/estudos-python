from moeda_calculo import dobro, aumentar, diminuir, metade


def start():
    print(
        f"o aumento de preço 10% foi de R$ {'400'} para {aumentar(423, 10, True)}")
    print(
        f"o preço de R$ {'423'} abaixou para 10% {diminuir(423, 10, True)}")
    print(f"o preço de R$ {'423'} dobrou para {dobro(423, True)}")
    print(f"a medade preço de R$ {'423'} é {metade(423, True)}")
