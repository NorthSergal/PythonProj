import sys  # Импорт модуля для работы с аргументами командной строки

outputString = "1"  # Строка для вывода
flag = -1  # Флаг
n = int(sys.argv[1])  # Значение кругового массива
m = int(sys.argv[2])  # Шаг

while flag % n != 1:  # Условие выхода появление единицы
    if flag % n != 0:
        outputString = outputString + str(
            flag % n)  # То в массив добавляется остаток от деления (число из кругового массива)
    else:
        outputString = outputString + str(
            flag % n + n)  # В массив добавляется остаток от деления плюс значение кругового массива (крайняя точка)
    flag = flag + m - 1  # К индексу прибавляется шаг на единицу меньше
print(outputString)
