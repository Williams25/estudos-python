expr = str(input("digite uma espressao "))

pilha = []

for simbolo in expr:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("expressao correta")
else:
    print("expressao incorreta")
