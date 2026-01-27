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
