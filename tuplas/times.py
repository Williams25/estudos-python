times = ("corinthians", "palmeiras", "santos", "gremio", "cruzeiro",
         "coritiba", "flamengo", "ponte preta", "atletico-go", "atletico-mg")

# times do brasileirao
print(times)
# mostrar os 5 primeiros times do brasileirao
print(times[:5])
# mostrar os 4 ultimos times do brasileirao
print(times[6:])
# mostrar em order alfabetica os times do brasileirao
print(sorted(times))
# mostrar a posição em que o corinthians se encontra
print(times.index("corinthians") + 1)
