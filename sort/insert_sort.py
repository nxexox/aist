#!/usr/bin/python
# coding: utf8


def insert_sort(_list):
    """
    Сортировка вставками.

    :param _list: Массив для сортировки.
    :type _list: list

    :return: Отсортированный массив.
    :rtype: list

    """
    for i in range(1, len(_list)):  # Надо начать со второго элемента.

        buf = _list[i]
        j = i - 1  # Начиная с элемента _list[i - 1]

        while j >= 0 and _list[j] > buf:  # Идем по массиву и ищем куда всунуть.
            _list[j + 1] = _list[j]  # Сдвигаем вправо на 1
            j -= 1

        _list[j + 1] = buf  # На свободное место записываем значение

    return _list


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(insert_sort(test_list))
