#!/usr/bin/python
# coding: utf8
"""
Тут находятся все метрики, которые мы будем использовать в алгоритмах поиска.
ВАЖНОЕ ЗАМЕЧАНИЕ. ЧАСТЬ МЕТРИК НЕОБХОДИМО БУДЕТ ДОПОЛНИТЕЛЬНО НОРМАЛИЗОВЫВАТЬ.

"""


def distance_levenshtein(str_one, str_two):
    """
    Расстояние Левенштейнаы между двумя строками str_one и str_two.
    Минимальное количество операций вставки одного символа,
    удаления одного символа и замены одного символа на другой,
    необходимых для превращения одной строки в другую.
    O(nm), O(nm) - Время, память.

    :param str_one: Первая строка для вчисления расстояния.
    :param str_two: Вторая строка для вычисления расстояния.
    :type str_one: str
    :type str_two: str

    :return: Итоговое расстояние между двумя строчками.
    :rtype: int

    """
    len_one, len_two = len(str_one), len(str_two)
    if len_one > len_two:
        # Меняем местами, что бы посторить правильную матрицу.
        # Где кол-во столбцов больше или равно кол-ву строк.
        str_one, str_two = str_two, str_one
        len_one, len_two = len_two, len_one
    matrix = [
        [i] + [0] * len_one if i != 0 else [j for j in range(len_one + 1)]
        for i in range(len_two + 1)
    ]  # Тут мы построили пустую матрицу, заполнив ее первый столбец и первую строку цифрами, остальное нулями.

    for i in range(1, len_two + 1):  # Идем, начиная со второй строки.
        for j in range(1, len_one + 1):  # Идем, начиная со второго столбца.
            if str_two[i - 1] == str_one[j - 1]:  # Если равны, просто копируем прошлое значение.
                matrix[i][j] = matrix[i - 1][j - 1]
            else:  # Иначе, определяем минимальное и прибавляем 1.
                del_char = matrix[i - 1][j]
                add_char = matrix[i][j - 1]
                change_char = matrix[i - 1][j - 1]
                matrix[i][j] = min((del_char, add_char, change_char)) + 1

    return matrix[len_two][len_one]


def distance_dameray_levenshtein(str_one, str_two):
    """
    Расстояние Дамерау-Левенштейна между двумя строками str_one и str_two.
    Минимальное количество операций вставки одного символа,
    удаления одного символа, замены одного символа на другой
    или транспозиции двух соседних символов,
    необходимых для превращения одной строки в другую.
    O(nm), O(nm) - Время, память.

    :param str_one: Первая строка для вчисления расстояния.
    :param str_two: Вторая строка для вычисления расстояния.
    :type str_one: str
    :type str_two: str

    :return: Итоговое расстояние между двумя строчками.
    :rtype: int

    """
    len_one, len_two = len(str_one), len(str_two)
    if len_one > len_two:
        # Меняем местами, что бы посторить правильную матрицу.
        # Где кол-во столбцов больше или равно кол-ву строк.
        str_one, str_two = str_two, str_one
        len_one, len_two = len_two, len_one
    matrix = [
        [i] + [0] * len_one if i != 0 else [j for j in range(len_one + 1)]
        for i in range(len_two + 1)
    ]  # Тут мы построили пустую матрицу, заполнив ее первый столбец и первую строку цифрами, остальное нулями.

    for i in range(1, len_two + 1):  # Идем, начиная со второй строки.
        for j in range(1, len_one + 1):  # Идем, начиная со второго столбца.
            if str_two[i - 1] == str_one[j - 1]:  # Если равны, просто копируем прошлое значение.
                matrix[i][j] = matrix[i - 1][j - 1]
            else:  # Иначе, определяем минимальное и прибавляем 1.
                del_char = matrix[i - 1][j]
                add_char = matrix[i][j - 1]
                change_char = matrix[i - 1][j - 1]
                # Т.к. максимальная, то не выпадет если ее не считать.
                transposition_char = max((del_char, add_char, change_char))
                # Если возможна транспозиция.
                if str_two[i - 1] == str_one[j - 2] and str_two[i - 2] == str_one[j - 1]:
                    transposition_char = matrix[i - 2][j - 2]  # Считаем.

                matrix[i][j] = min((del_char, add_char, change_char, transposition_char)) + 1

    return matrix[len_two][len_one]


if __name__ == "__main__":
    print(distance_levenshtein("OPAP", "OPPA"))
    print(distance_dameray_levenshtein("OPAP", "OPPA"))
