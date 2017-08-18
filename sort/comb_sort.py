#!/usr/bin/python
# coding: utf8


def comb_sort(_list):
    """
    Сортировка расческой. Сортируем по два элемента на расстонии d.

    :param _list: Массив для сортировки
    :type _list: list

    :return: Отсортированный массив
    :rtype: list

    """
    length = len(_list)  # Расстояние между элементами.

    while length > 1:
        length = max(1, int(length / 1.25))  # Расстояние должно быть минимум 1.

        for i in range(len(_list) - length):  # Идем не по всей длине, что бы не выскочить за массив.
            if _list[i] > _list[i + length]:  # Смотрим надо ли поменять местами.
                _list[i], _list[i + length] = _list[i + length], _list[i]

    return _list


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(comb_sort(test_list))
