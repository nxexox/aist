#!/usr/bin/python
# coding: utf8


def shell_sort(_list):
    """
    Сортировка Шелла. Сортируем подгруппы элементов на расстонии d.

    :param _list: Массив для сортировки.
    :type _list: list

    :return: Отсортированый массив.
    :rtype: list

    """
    length = len(_list)
    d = int(length // 2)

    while d > 0:  # Пока есть расстояние
        for i in range(length - d):  # Идем под подгруппе

            j = i
            while j >= 1 and _list[j] > _list[j + d]:  # Внутри подгруппы сортируем элементы.
                _list[j], _list[j + d] = _list[j + d], _list[j]
                j -= 1

        d = int(d // 2)

    return _list


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(shell_sort(test_list))
