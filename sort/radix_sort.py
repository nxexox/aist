#!/usr/bin/python
# coding: utf8


def radix_sort(_list):
    """
    Поразрядная сортировка MSD для целых числ десятичной системы.

    :param _list: Массив для сортировки
    :type _list: list

    :return: Отсортированный массив
    :rtype: list

    """
    k = len(str(max(_list)))  # Максимальный разряд числа
    rang = 10  # Мощность алфавита десятичных чисел.

    for i in range(k):
        buf_list = [[] for _ in range(rang)]  # Массив для деления по числам

        for number in _list:
            buf_list[number // 10 ** i % 10].append(number)  # Определяем куда сунуть и суем
        _list = []  # Обнуляем исходный

        for index in range(rang):  # Склеиваем обратно
            _list.extend(buf_list[index])

    return _list

if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(radix_sort(test_list))
