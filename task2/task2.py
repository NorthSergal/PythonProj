import sys  # Импорт модуля для работы с аргументами командной строки

global file1  # Объявление глобальных переменных для расширение зоны видимости в блоке TRY
global file2
try:
    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')
except FileNotFoundError:
    print("Ошибка открытия файла. Файл не найден.")
except IndexError:
    print("Неверное число аргументов")

xOne, yOne = file1.readline().split()  # Присвоение значеиний координат центра окружности
xOne = float(xOne)  # Приведение строки к числу с плавающей точкой
yOne = float(yOne)
radius = file1.readline()  # Присвоение значения радиуса
radius = float(radius)

dotCoordinats = file2.readline()  # Считывание первой строки файла с точками

for line in file2:  # Для каждой строки файла
    xTwo, yTwo = dotCoordinats.split()  # Разделение значений в одной строке
    xTwo = float(xTwo)  # Приведение староки к числу с плавающей точкой
    yTwo = float(yTwo)
    if (xTwo - xOne) * (xTwo - xOne) + (yTwo - yOne) * (yTwo - yOne) == radius * radius:  # Мат вычисления
        print(0)
    elif (xTwo - xOne) * (xTwo - xOne) + (yTwo - yOne) * (yTwo - yOne) < radius * radius:
        print(1)
    else:
        print(2)

file1.close()  # Закрытие открытых файлов
file2.close()
