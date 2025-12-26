# Порядок выполнения операций в алгебре логики
# 1. Отрицание / Инверсия (¬A, (not A))
# 2. Логическое умножение / Конъюнкция (A∧B, A∙B, A and B)
# 3. Логическое сложение / Дизъюнкция (A∨B, A+B, A or B)
# 4. Следование / Импликация (A→B, A <= B)
# 5. Тождество / Эквивалентность (A≡B, A == B)

# Исключающее или / XOR (A ⊕ B, A ^ B)


# Порядок выполнения операций в Python
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. in, not in
# 6. ==, !=, >, >=, <, <=
# 7. ^
# 8. not
# 9. and
# 10. or

# решение через лесенку
print('a b c d')
for a in range(2):
    for b in (0,1):
        for c in [0,1]:
            for d in 0,1:
                f = (not a and not b) or (b==c) or d
                # все строки истины
                if f:
                    print(a,b,c,d)
                # все строки ложны
                if not f:
                    print(a,b,c,d)
                # строки вперемешку
                print(a,b,c,d)

# args
def f1(a, b, c):
    return a + b + c


test1 = [1, 2, 3]
print(f1(*test1))

# kwargs
def f2(a, b):
    return a / b

test2 = {'b': 2, 'a': 1}
print(f2(**test2))

from itertools import product, permutations

def f(x,y,w,z):
    return (x and (not y)) or (y == z) or not w

for i in product((0,1), repeat=4):
    table = [
        (i[0],i[1], 0, 0),
        (1, 0, i[2], 0),
        (1, 0, 1, i[3])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            # zip(p, t) - сопоставляет заголовки из p c значениями из t;
            # dict(zip(p, t)) - преобразует zip объект в базовый тип данных (словарь);
            # f(**dict(zip(p, t))) - распаковывает через kwargs все ключи в функцию;
            if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
                print(*p,sep='')
