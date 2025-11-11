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
num_tri='111'
num_hex='fa8'
print(int(num_bin,2))
print(int(num_tri,3))
print(int(num_hex,16))

# срезы
data='123456789'

# извлечение первых двух символов
print(data[:2])

# извлечение без первых двух символов
print(data[2:])

# извлечение последних двух символов
print(data[-2:])

# извлечение без последних двух символов
print(data[:-2])

# сумма цифр числа
# двоичная система
num_1='1010'
sum_1=num_1.count('1')

# любая система до 10 включительно
num_2='193'
sum_2= sum(map(int,num_2))
print(sum_2)

# любая система до 36 включительно
num_3='AF5'
print(int(num_3,36))
sum_3= sum(map(lambda x: int(x,36),num_3))