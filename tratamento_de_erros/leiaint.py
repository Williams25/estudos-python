def leiaInt():
    while True:
        try:
            num = int(input("Digite um numero: "))
        except (ValueError, TypeError):
            print(f"\nValor incorreto")
            continue
        except KeyboardInterrupt:
            print(f"\nValor não informado")
            break
        else:
            return num


def leiaFloat():
    while True:
        try:
            num = float(input("Digite um numero: "))
        except (ValueError, TypeError):
            print(f"\nValor incorreto")
            continue
        except KeyboardInterrupt:
            print(f"\nValor não informado")
            break
        else:
            return num


leiaInt()
