# -*- coding: utf-8 -*-
"""Копия блокнота ""Практика 0.2.0 .ipynb""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16sweadJxNSOA0OfnXJBlfPdmP2vyYp5L

Напишите свое ФИО:
"""

Елгин Никита Сергеевич

"""# Основы

Задание 1: Напиши программу, выводящую на экран сообщение "Привет, мир!"
"""

print("Привет, мир!")

"""Задание 2: Напиши программу которая запрашивает имя пользователя и выводит сообщение:

`Привет, <Имя пользователя>`
"""

name = input("введите имя пользователя:")
print('Привет,', name)

"""Задание 3: Напиши программу определяющую является ли число четным или нечетным:

Пример:

`Введите число:` 2

`Ваше число четное!`
"""

number = int(input('Введите число:'))
if number % 2 == 0:
  print('Ваше число четное!')
else:
  print('Ваше число нечетное!')

"""Задание 4: Напишите программу которая запрашивает длинну и ширину прямоугольника и выводит его площадь:



`Введите длинну прямоугольника:`

`Введите ширину прямоугольника:`

`Площадь прямоугольника: `


"""

side_one = int(input('Введите длинну прямоугольника:'))
side_two = int(input('Введите ширину прямоугольника:'))
print('Площадь прямоугольника:', side_one * side_two)

"""Задание 5: Напишите программу, которая будет вычислять среднее арифметическое введенных чисел"""

list1 = [int(i) for i in input('введите числа через пробел:').split()]
sum_list = sum(list1)
print(int(sum_list / len(list1)))

"""Задание 6: Напиши программу, которая бы определяла является ли год високосным"""

year = int(input('введите необходимый год:'))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('год является високосным')
else:
    print('год неявляется високосным')

"""Задание 7: Необходимо создать простой калькулятор, который позволяет пользователю выбрать одну из четырёх операций (+, -, *, /), ввести два числа и получить результат выполнения операции."""

number1, number2 = map(int,input('введите два числа через пробел которые необходимо перемножить:').split())
print(number1 * number2)

"""--------------------------------------------------------------------------------

**Да, задания ниже тоже обязательны, вам необходимо выполнить веееееесь файл**

--------------------------------------------------------------------------------

# Практика 0.2.1

**Шахматы**

Даны стартовые и конечные координаты, а также фигура

Необходимо определить, может ли заданная фигура так ходить?
"""

kt1, kt2, figure = input('введите стартовые и конечные координаты и название фигуры (пример:2b 5b пешка):').split()
letter_board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
letter_kt1, letter_kt2 = str(kt1[1]), str(kt2[1])
number_kt1, number_kt2 = int(kt1[0]), int(kt2[0])
letter_kt1, letter_kt2 = letter_board.index(letter_kt1) + 1, letter_board.index(letter_kt2) + 1
if letter_kt1 < 9 and letter_kt2 < 9 and number_kt1 < 9 and number_kt2 < 9:
  if figure == 'пешка':
    if number_kt1 + 1 == number_kt2 and letter_kt1 == letter_kt2 or number_kt1 == 2 == number_kt2 - 2 and letter_kt1 == letter_kt2:
      print('+')
    else:
      print('-')
  elif figure == 'ладья':
    if number_kt1 != number_kt2 and letter_kt1 == letter_kt2 or number_kt1 == number_kt2 and letter_kt1 != letter_kt2:
      print('+')
    else:
      print('-')
  elif figure == 'король':
    if abs(number_kt1 - number_kt2) <= 1 and abs(letter_kt1 - letter_kt2) <= 1:
      print('+')
    else:
      print('-')
  elif figure == 'слон':
    if number_kt1 - number_kt2 == letter_kt1 - letter_kt2 or (number_kt1 - number_kt2)/-1 == letter_kt1 - letter_kt2 or number_kt1 - number_kt2 == (letter_kt1 - letter_kt2)/-1:
      print('+')
    else:
      print('-')
  elif figure == 'конь':
    if abs(number_kt1 - number_kt2) == 1 and abs(letter_kt1 - letter_kt2) == 2 or abs(number_kt1 - number_kt2) == 2 and abs(letter_kt1 - letter_kt2) == 1:
      print('+')
    else:
      print('-')
  elif figure == 'королева':
    if (abs(number_kt1 - number_kt2) == abs(letter_kt1 - letter_kt2) or number_kt1 == number_kt2 or letter_kt1 == letter_kt2) or (abs(number_kt1 - number_kt2) <= 1 and abs(letter_kt1 - letter_kt2) <= 1):
      print('+')
    else:
      print('-')
else:
  print('-')

"""# Практика 0.2.2

**Цифра на определенном месте:**

Последовательно записан натуральный ряд чисел.

Какая цифра стоит в N позиции
"""

lst = [int(i) for i in input().split()]
N = int(input('введите номер необходимой позиции числа:'))
print(lst[N-1])

"""# Практика 0.2.3


Возьмите код из задания 7 и улучшите ваш калькулятор следующим образом:

Пользователь вводит строку вида:

(5+5)*5 - данная строка содержит в себе математическое выражение, а также скобки

Ваша программа должная понять что за математическое выражение записано, проверить верно ли оно записано (пример неверного заполнения: (5(+)5)*5, а также расчитать его в соотвествии с правилами математики
"""

