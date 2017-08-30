#!/usr/bin/python
# coding: utf8
"""
Поиск k-го элемента порядковой статистики на неупорядоченном множестве.
Сложность O(n) по времени. И O(1) по памяти.

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


if __name__ == "__main__":
    test_list = [1, 10, 2, 20, 3, 40, 23, 43, 44, 201, 12, 11, 3, 405, 42, 61, 90]
    print("3: ", knt(test_list, 0, len(test_list) - 1, 3))
    print("10: ", knt(test_list, 0, len(test_list) - 1, 10))
    print("7: ", knt(test_list, 0, len(test_list) - 1, 7))
    # Принтуем отсортированный для проверки
    test_list.sort()
    print(test_list)
