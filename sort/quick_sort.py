#!/usr/bin/python
# coding: utf8


def quick_sort(_list):
    """
    Быстрая сортировка.

    :param _list: Массив для сортировки.
    :type _list: list

    :return: Отсортированный массив.
    :rtype: list

    """
    if len(_list) <= 1:
        return _list

    pseudo_median = _list[len(_list) // 2]
    l, r, m = [], [], []

    for i in _list:
        if i < pseudo_median:
            l.append(i)
        elif i > pseudo_median:
            r.append(i)
        else:
            m.append(i)

    return quick_sort(l) + m + quick_sort(r)


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(quick_sort(test_list))
