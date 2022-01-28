import sys  # Импорт модуля для работы с аргументами командной строки


def searcher(id):  # Функция выделение VALUE
    global papir2  # Объявление глобальных переменных для расширение зоны видимости в блоке TRY
    try:
        papir2 = open(sys.argv[2], 'r')  # Откртие файла VALUES.JSON
    except FileNotFoundError:
        print("Указанный файл не найден")
    except IndexError:
        print("Неверное число аргументов")

    lines = papir2.readlines()  # Считывание всех строк файла

    pattern = " " + str(id) + ","  # Сотставление шаблона поиска

    for i in range(len(lines)):  # Для каждой строки файла
        if pattern in lines[i]:
            value_arr = lines[i + 1].split('"')  # Разбитие строки на слова
            value = value_arr[3]  # Выбор значения

    papir2.close()

    return value


id = 0

global papir1
try:
    papir1 = open(sys.argv[1], 'r')
except FileNotFoundError:
    print("Указанный файл не найден")
except IndexError:
    print("Неверное число аргументов")

papir3 = open("report.json", 'a', encoding='utf-8')  # Открытие / Создание файла на дозапись

for line in papir1:

    if line.find('"id"') == -1:  # Если шаблон '"id"' не найден

        if line.find('"value"') != -1:  # Если шаблон '"value"' найден
            value = searcher(id)  # Вызов функции
            papir3.write(
                line[:line.find('"value"') + 10] + value + line[line.find('""') + 1:])  # Запись строки с форматом
        else:
            papir3.write(line)  # Копирование строки без изменений

    elif line.find('"id"') != -1:  # Если шаблон '"id"' найден

        id = line[line.find('"id"') + 6:len(line) - 2]  # Вычленение  ID
        papir3.write(line)

papir1.close()  # Закрытие файлов
papir3.close()
