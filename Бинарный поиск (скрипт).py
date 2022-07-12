# ПОИСК ЗА КАКОЕ КОЛЛИЧЕСТВО ПОПЫТОК МОЖНО УГАДАТЬ ЗАДАННОЕ ЧИСЛО
from random import *
num = randint(1, 100)
counter = 0
left = 1
right = 100

while True:
    counter += 1
    middle = (left + right) // 2
    if middle == num:
        print('Загаданное число >> ', num, ',', ' будет угадано за >> ', counter, ' попыток', sep='')
        break
    elif middle < num:
        left = middle + 1
        continue
    elif middle > num:
        right = middle - 1
        continue

# БЫСТРЫЙ СПОСОБ С ВВЕДЕННЫМ ЧИСЛОМ
from math import *
n = int(input())
x = ceil(log2(n))
print(x)


