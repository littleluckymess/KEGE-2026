# Задачи с масками

# Библиотека для проверки строк под маску
from fnmatch import fnmatch

# ? - ровно один любой символ
# * - любое кол-во любых символов


# КомпЕГЭ 4603 (рекомендованное решение)
from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
    if fnmatch(str(N), '1234*7'):
        print(N, N // 141)

# Алгоритм для определения стартовой позиции:
# Из шаблона составляем самое маленькое число (* заменяем на ничего, ? заменяем на 0)
# Из числа вычитаем остаток деления, чтобы получить ближайшее кратное число

#########################################
print('##################################')

# КомпЕГЭ 4603 (решение перебором)
from itertools import product
from string import printable

ans = []
for l in range(0, 4):
    for Z in product(printable[:10], repeat=l):
        num = int('1234' + ''.join(Z) + '7')
        if num % 141 == 0 and num <= 10 ** 8:
            ans.append([num, num // 141])

for i in sorted(ans):
    print(*i)


##############################################################

# Задачи с делителями
def f(num):
    d = set()
    # Перебор делителей числа
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            # | - объединение множеств
            d |= {i, num // i}


# Проверка чисел на простоту
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(1))


# Разложение числа на простые множители (медленный способ)
def fact_1(num):
    d = []

    for i in range(2, int(num ** .5) + 1):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]

    return d


# Разложение числа на простые множители (менее медленный способ)
def fact_2(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    for i in range(3, int(num ** .5) + 1, 2):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]

    return d


# Разложение числа на простые множители (быстрый способ)
def fact_3(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d
