from itertools import*
# product - функция, которая формирует
# всевозможные комбинации символов с повторениями длины repeat
alph = '12'
for val in product(alph, repeat=2):
    val = ''.join(val)

# permutations - функция, которая формирует
# # всевозможные комбинации символов
for val in permutations(alph):
    val = ''.join(val)

# enumerate - нумерует элементы, начиная от start
res = enumerate(alph, start=1)
print(*res)