try:
    a = int("Numerador: ")
    b = int("Denominador: ")
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que voce digitou")
except ZeroDivisionError:
    print("Nao é possivel dividir um numero por 0")
except KeyboardInterrupt:
    print("O usuario não informou os dados")
except Exception as erro:
    print(f"Ocorreu um erro {erro.__class__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("volte sempre")
