def minNum():
  firstNum = int(input("Введите значение первого числа: "))
  secondNum = int(input("Введите значение второго числа: "))
  thirdNum = int(input("Введите значение третьего числа: "))
  if firstNum > secondNum > thirdNum:
    print(f"{thirdNum} является наименьшим значением из приведённых чисел.")
  elif thirdNum > secondNum > firstNum:
    print(f"{firstNum} является наименьшим значением из приведённых чисел.")
  else:
    print(f"{secondNum} является наименьшим значением из приведённых чисел.")

def quadEquation():
  firstNum = int(input("Введите значение первого коэффицента квадратного уравнения: "))
  secondNum = int(input("Введите значение второго коэффицента квадратного уравнения: "))
  thirdNum = int(input("Введите значение третьего коэффицента квадратного уравнения: "))
  discriminant = secondNum ** 2 - (4 * firstNum * thirdNum)
  if (discriminant >= 0):
    print("Да.")
  else:
    print("Нет.")

def wholeDiv():
  firstNum = int(input("Введите значение переменной m: "))
  secondNum = int(input("Введите значение переменной n: "))
  try:
    if firstNum / secondNum == firstNum // secondNum and firstNum / secondNum > 0:
      print(f"m делённая на n равна {firstNum / secondNum}")
    else:
      print(f"m на n нацело не делится. Произведение чисел равно {firstNum * secondNum}")
  except ZeroDivisionError:
    print("На ноль делить нельзя.")

def threeDigitNum():
  singleNum = int(input("Введите число: "))
  if 99 < singleNum < 1000:
    print("Введённое число является трёхзначным.")
  else:
    print("Введённое число не является трёхзначным.")

def numsTime():
  firstNum = int(input("Введите значение времени в секундах: "))
  secondNum = int(input("Введите значение времени в минутах: "))
  if firstNum < secondNum * 60:
    print("Значение времени в минутах больше значения времени в секундах.")
  elif firstNum == secondNum * 60:
    print("Значение времени в минутах равно значению времени в секундах.")
  else:
    print("Значение времени в минутах меньше значения времени в секундах.")