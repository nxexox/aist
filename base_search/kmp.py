#!/usr/bin/python
# coding: utf8
"""
Кнута-Мориа-Прада(КМП)
O(M + N)

"""


def prefix_function(string):
    """
    Префикс функция.

    :param string: Строка, для которой надо вычислить префикс функцию.
    :type string: str

    :return: Вычисленную префикс функцию.
    :rtype: list

    """
    result = [0]  # Нулевой элемент опускаем, он равен сам себе.

    for i in range(1, len(string)):

        j = result[i - 1]  # эту строку мы заменили

        while j > 0 and string[j] != string[i]:
            j = result[j - 1]
        if string[j] == string[i]:
            j += 1

        result.append(j)

    return result


def kmp_search(needle, haystack):
    """
    Поиск КМП.
    Возвращает индекс найденной строки либо None, если строка не найдена.

    :param needle: Искомая подстрока.
    :param haystack: Строка, в которой ищем.
    :type needle: str
    :type haystack: str

    :return: Индекс первого найденного вхождения.
    :rtype: int

    """
    d = prefix_function(needle)
    i = j = 0

    while i < len(haystack) and j < len(needle):  # Пока не найдем или не достигнем конца.
        if needle[j] == haystack[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j - 1]

    if j == len(needle):
        return i - j - 1

    return None


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuestamvvmtestkllkgggootestnmnmtestnjhhkkteskjlktestkljkgljh"
    prefix_test = "ababcaba"
    print(prefix_function(prefix_test))  # Префикс функция.
    print(kmp_search(needle, haystack))  # Поиск КМП.
