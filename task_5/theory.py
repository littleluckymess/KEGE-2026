# системы счисления

# двоичная система
N=25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])

# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{N:b}')

# восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

# перевод в любую систему (2<= sys <=9)
def convert(num,sys):
    res = ''
    while num !=0:
        res += str(num % sys)
        num //= sys
    return res[::-1]



# перевод в любую систему (2<= sys <=36)
from string import printable as alph
def convert2 (num,sys):
    res = ''
    while num !=0:
        res += alph [num % sys]
        num //= sys
    return res[::-1]

# перевод в десятичную систему
num_bin='101'
num_tri='121'
num_hex='fa8'
print(int(num_bin,2))
print(int(num_tri,2))
print(int(num_hex,2))