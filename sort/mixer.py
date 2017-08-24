#!/usr/bin/python
# coding: utf8
"""
Функция перемешивания массива.
Критерий, максимум два подряд отсортированных элемента, если такое возможно.

"""


def knt(_list, l, r, k):
    """
    Средненький Алгоритм поиска k-й порядковой статистики.
    Модификация быстрой сортировки.

    :param _list: Массив в котором ищем.
    :param l: Граница массива слева.
    :param r: Граница массива справа.
    :param k: Наша позиция k.

    :return: Значение k-го наимешьшего порядкового элемента.
    :rtype; int

    """
    x = _list[(l + r) // 2]  # Берем псевдомедиану.
    i, j = l, r

    while i <= j:
        while _list[i] < x:
            i += 1
        while _list[j] > x:
            j -= 1

        if i <= j:
            _list[i], _list[j] = _list[j], _list[i]
            i += 1
            j -= 1

    if l <= k <= j:
        return knt(_list, l, j, k)
    if i <= k <= r:
        return knt(_list, i, r, k)

    return _list[k]


def mixer(_list):
    """
    Функция перемешивания массива. Все просто.
    Берем нулевой элемент по порядковой статистике, и послежний, ставим друг за другом.
    Потом берем первый и предпоследний, и так пока не дойдем до середины.
    Оценка O(n*n)

    :param _list: Массив для перемешивания.
    :type _list: list

    :return: Перемешанный массив.
    :rtype: list

    """
    len_list = len(_list)
    result = []

    for i in range(len_list // 2):
        l, r = knt(_list, 0, len_list - 1, i), knt(_list, 0, len_list - 1, len_list - i - 1)
        result.append(l)
        result.append(r)

    return result


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(mixer(test_list))  # Перемешивание массива.
