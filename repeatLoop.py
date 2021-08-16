frutas = ["laranja", "maçã", "melancia", "melão", "pera"]
print(frutas)

for i in frutas:
  print(i)

numbers = []

def timesTables (targert: int, rangeNumber: int) -> str:
  for i in range(rangeNumber + 1):
    numbers.append("{0} * {1} = {2}".format(targert, i, targert * i))

timesTables(5, 10)

print(numbers)

count = 0

while count <= 10:
  print("Menor que 10 {}".format(count))
  if (count == 6):
    print("Contador igual a {} então para de contar".format(count))
    break
  count += 1

if (count >= 10):
  print("Maior que 10 valor atual é {}".format(count))


def factorialNumber (factorial: int) -> int:
  number = factorial
  factorialCount = 1
  
  while (number - factorialCount) > 1:
    factorial = (factorial * (number - factorialCount))
    factorialCount += 1

  return factorial

print(factorialNumber(4))