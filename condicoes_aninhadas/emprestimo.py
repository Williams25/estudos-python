class Emprestimo:
    def __init__(self, casa, salario, anos):
        self.casa = casa
        self.salario = salario
        self.anos = anos
        self.prestacao = casa / (anos * 12)
        self.minimo = salario * 30 / 100

    def validar_emprestimo(self):
        if self.prestacao <= self.minimo:
            print("Emprestimo concedido")
        else:
            print("Emprestimo não aprovado")


casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual seu salario? R$"))
anos_a_pagar = int(input("Em quantos anos quer pagar? "))

prestacao = casa / (anos_a_pagar * 12)
minimo = salario * 30 / 100

emprestimo = Emprestimo(casa, salario, anos_a_pagar)
emprestimo.validar_emprestimo()

print("Para pagar a casa de R${:.2f} em {} anos".format(
    emprestimo.casa, emprestimo.anos))
print("o valor será de R${:.2f}".format(emprestimo.prestacao))
