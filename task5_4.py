# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!

def summ_line(n, el, sum):
    if n == 0:
        return sum
    sum = sum + el
    el = el * -0.5
    n = n - 1
    return summ_line(n, el, sum)


try:
    n = int(input("Введите количество элемнтов ряда: "))
    summa = summ_line(n, el=1, sum=0)
    print(f"Сумма элементов ряда равна: {summa} ")
except ValueError:
    print("Неправильно введены данные")
