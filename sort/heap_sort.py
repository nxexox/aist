#!/usr/bin/python
# coding: utf8


def heap_sort(_list):
    """
    Пирамидальная сортировка. Строим CБД слева направо.
    По закону: a[i] >= a{2*i + 1] and a[i] >= a[2*i + 2]. Иначе говоря, это КУЧА.
    2 этапа. Постороение пирамиды, Сортировка

    :params _list: Массив для сортировки.
    :type _list: list

    :return: Отсортированный массив.
    :rtype: list

    """
    length = len(_list)

    # Меняем местами.
    def swap(pi, ci):
        if _list[pi] < _list[ci]:
            _list[pi], _list[ci] = _list[ci], _list[pi]

    # Просеивание через КУЧУ.
    def sift(index, unsorted):
        while index * 2 + 2 < unsorted:
            gtci = max(_list[index * 2 + 1], _list[index * 2 + 2])
            swap(index, gtci)
            index = gtci

    # Строим пирамиду. Правая часть дерева n/2 - 1
    for i in range(int((length / 2)) - 1, -1, -1):
        sift(i, length)

    # sort
    for i in range(length - 1, 0, -1):
        swap(i, 0)
        sift(0, i)

    return _list


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(heap_sort(test_list))
