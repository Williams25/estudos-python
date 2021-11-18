import dado
from moeda_calculo import dobro, aumentar, diminuir, metade, formatar_moeda

valor = dado.leiaDinheiro('Digite o preço R$ ')

print(
    f"o aumento de preço 10% foi de {formatar_moeda(valor)} para {aumentar(valor, 10, True)}")
print(
    f"o preço de {formatar_moeda(valor)} abaixou para 10% {diminuir(valor, 10, True)}")
print(f"o preço de {formatar_moeda(valor)} dobrou para {dobro(valor, True)}")
print(f"a medade preço de {formatar_moeda(valor)} é {metade(valor, True)}")
