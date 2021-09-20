# 7.Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
from itertools import count
from math import factorial
def factgen():
    for el in count(1):
        yield factorial(el)
gen = factgen()
n = 0
for elem in gen:
    if n < 6:
        print(elem)
        n += 1
    else:
        break