#!/usr/bin/python
# coding: utf8
"""
Алгоритм прямого поиска. Решение в лоб.

"""


def base_search(needle, haystack):
    """
    Алгоритм прямого поиска.
    Возвращает индекс найденной строки либо None, если строка не найдена.

    :param needle: Искомая подстрока.
    :param haystack: Строка, в которой ищем.
    :type needle: str
    :type haystack: str

    :return: Индекс первого найденного вхождения.
    :rtype: int

    """
    result_index = 0
    result_search = False
    len_h = len(haystack)
    len_n = len(needle)
    i = 0

    while i < len_h and not result_search:  # Идмем по строке в которой ищем.
        for index, j in enumerate(needle):  # Сравниваем поэлементно.
            if haystack[i + index] == j:
                result_index = i
            else:
                break
            if index + 1 == len_n:
                result_search = True
        i += 1

    return result_index - 1 if result_search else None


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuestamvvmtestkllkgggootestnmnmtestnjhhkkteskjlktestkljkgljh"
    print(base_search(needle, haystack))
