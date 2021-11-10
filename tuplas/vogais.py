palavras = (
    "aprender",
    "programar",
    "estudar",
    "linguagem",
    "python",
    "trabalhar",
    "mercado"
)

for p in palavras:
    print("\nna palavra {} temos as seguintes vogais ".format(p.upper()), end="")

    for letra in p:
        if letra.lower() in "aeiou":
            print("{}".format(letra), end=" ")
