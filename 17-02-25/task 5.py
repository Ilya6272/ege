# Перевод в другие системы счисления (2 <= sys <= 9)
def convert(num, sys):
     res = ''
     while num:
         res += str(num % sys)
         num //= sys
     return res[::-1]

from string import digits, ascii_uppercase
# Перевод в другие системы счисления (2 <= sys <= 36)
def convert(num, sys):
    alph = digits + ascii_uppercase
     res = ''
     while num:
         res += alph[num % sys]
         num //= sys
     return res[::-1]


num = 17
num2 = bin(num)[2:] # двоичная
num3 = oct(num)[2:] # восьмеричная
num4 = hex(num)[2:] # шестнадцатеричная


# Перевод обратно в десятичню систему
num5 = '10101'
print(int(num5, 2))




