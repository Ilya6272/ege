# Подключение библиотеки для комбинаторики
from itertools import product

# Расстановка символов в алфавитном порядке
alph = sorted('МАНГУСТ')

cnt = 0 # Счётчик кол-ва слов
# Формируем все шестибуквенные слова
for i in product(alph, repeat=6):
    # Каждое новое слово увеличивает счётчик на один
    # Это позволит нам пронумеровать каждое слово и получить ответ
    cnt += 1
    # Обязательная строка. Заменяет кортеж i на строку i
    i = ''.join(i)
    # Переписываем условия из задания
    if i[0] != 'У' and i.count('М') == 2 and i.count('Г') <= 1:
        print(cnt, i)
