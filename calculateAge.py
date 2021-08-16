from datetime import datetime

questionAge = int(input("Que ano você nasceu?"))

def calculateAge (age: int) -> str:
  now = datetime.now()
  currentAge = now.year - age

  if (currentAge>= 18 and currentAge <= 100):
    return "você tem mais que 18 anos sua idade atual é {} anos".format(currentAge)
  elif (currentAge >= 100 or currentAge <= 0): 
    return "idade {} inválida".format(currentAge)
  elif (currentAge<= 17):
    return "você não tem mais que 18 anos sua idade atual é {} anos".format(currentAge) 
  else:
    return "paramentro inválido"

print(calculateAge(questionAge))