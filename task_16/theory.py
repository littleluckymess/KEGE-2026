# По умолчанию глубина рекурсии не может превышать 1000
# Мы можем расширить кол-во шагов при помощи:
from sys import setrecursionlimit

steps_amount = 2000
setrecursionlimit(steps_amount)

# Значение steps_amount высчитывается по формуле:
# steps_amount = ceil(N / step) + 1, где
# N - самое большое число, которое передается функции.
# step - значение, на которое увеличивается/уменьшается число при вызове нового шага рекурсии.
# Данный способ ок, если steps_amount не более двух тысяч, в других случаях нужен lru_cache

# 21415

from sys import setrecursionlimit

def F(n):
    if n <= 5: return 1
    return n + F(n - 2)

setrecursionlimit(1100)
print(F(2126) - F(2122))


# Кэширование промежуточных результатов
#   from functools import lru_cache
#   @lru_cache(None)

# 27076

from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 43: return G(n + 4)
    return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11_240: return G(n + 3) + 2
    return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21: return n + 4
    return Q(n - 4) + 2

for i in range(20, 11_240):
    Q(i)

for i in range(11_240, 42, -1):
    G(i)

for i in range(42, 2026):
    F(i)

print(F(2026))

# Альтернативный способ без функций - 27076

F = [0] * 2_500
G = [0] * 12_000
Q = [0] * 12_000

for i in range(0, 12_000):
    if i < 21: Q[i] = i + 4
    else: Q[i] = Q[i - 4] + 2

for i in range(1, 12_000)[::-1]:
    if i < 11_240: G[i] = G[i + 3] + 2
    else: G[i] = Q[i]

for i in range(1, 2_500):
    if i < 43: F[i] = G[i + 4]
    else: F[i] = 2 * F[i - 2] - F[i - 4] + 2

print(F[2026])