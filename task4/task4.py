import sys  # Импорт модуля для работы с аргументами командной строки

global fileArray  # Объявление глобальных переменных для расширение зоны видимости в блоке TRY
try:
    fileArray = open(sys.argv[1], 'r')  # Файл откуда считываются значеения массива
except FileNotFoundError:
    print("Указанный файл не найден")
except IndexError:
    print("Неверное число аргументов")

numes = []  # Объявление массива
mediana = 0
itog = 0
itog2 = 0

for line in fileArray:  # Для каждой строки файла
    numes.append(int(line))  # Добавление значения в массив

numes.sort()  # Сортировка масссива

n = len(numes)
index = n // 2  # Поиск середины массива

if n % 2:  # Если массив четный
    mediana = sorted(numes)[index]  # Медиана - значение посередине
    for num in numes:
        itog = abs(num - mediana) + itog  # Вычисление итога

else:
    mediana = sum(sorted(numes)[index - 1:index + 1]) / 2  # Медиана - среднее двух значений
    for num in numes:  # Для каждого элемента массива
        itog = abs(num - index - 1) + itog  # Подсчет итога для двух значений
        itog2 = abs(num - index + 1) + itog2
if itog > itog2 and itog2 != 0:  # Сравнение и вывод  меньшего итога
    print(itog2)
else:
    print(itog)

fileArray.close()
