import task_module as mod

choice = int(input("Выберите любое задание из предложенного списка: \n 1. Минимальное из трёх заданных число; \n 3. Корни квадратного уравнения; \n 4. Деление чисел нацело; \n 7. Трёхзначное число; \n 8. Сравнение времени с различными измерительными величинами.")) 
if choice == 1:
  mod.minNum()
elif choice == 3:
  mod.quadEquation()
elif choice == 4:
  mod.wholeDiv()
elif choice == 7:
  mod.threeDigitNum()
elif choice == 8:
  mod.numsTime()
else:
  print(f"{choice} по номеру задания нет.")