from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:19]:
    num1 = int('988897' + x + '21' ,19)
    num2 = int('2' + x + '923', 19)
    num = num1 + num2
    if num % 18 == 0:
        print(num // 18)
