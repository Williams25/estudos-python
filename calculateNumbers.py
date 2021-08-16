def calculate (num1: int, num2: int, operation: str) -> int:
  total = 0
  if (operation == "sum"):
    total = num1 + num2
  elif (operation == "sub"):
    total = num1 - num2
  elif (operation == "mult"):
    total = num1 * num2
  elif (operation == "div"):
    total = num1 / num2
  return total

print(
  "executando function",
  calculate(5, 8, "div"), 
  calculate(5, 8, "mult"),
  calculate(5, 8, "sub"),
  calculate(5, 8, "sum")
)