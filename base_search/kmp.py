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
    index = -1
    f = prefix_function(needle)
    k = 0

    for i in range(len(haystack)):

        while k > 0 and needle[k] != haystack[i]:
            k = f[k - 1]
        if needle[k] == haystack[i]:
            k = k + 1
        if k == len(needle):
            index = i - len(needle) + 1
            break

    return index


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuestamvvmtestkllkgggootestnmnmtestnjhhkkteskjlktestkljkgljh"
    prefix_test = "ababcaba"
    print(prefix_function(prefix_test))  # Префикс функция.
    print(kmp_search(needle, haystack))  # Поиск КМП.
