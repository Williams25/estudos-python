lista = []

for i in range(0, 5):
    num = int(input("digite um numero "))

    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print("-"*30)
print(f"lista ordenada {lista}")
print("-"*30)
