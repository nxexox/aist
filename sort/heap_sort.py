#!/usr/bin/python
# coding: utf8


def heap_sort(_list):
    """
    Пирамидальная сортировка. Строим CБД слева направо.
    По закону: a[i] >= a{2*i + 1] and a[i] >= a[2*i + 2]. Иначе говоря, это КУЧА.
    2 этапа. Постороение первичной пирамиды, Вытеснение максималного, перестроение.

    :param _list: Массив для сортировки.
    :type _list: list

    :return: Отсортированный массив.
    :rtype: list

    """
    def swap_items(index1, index2):
        """
        Меняем местами два элемента.

        :param index1: Индекс левого элемента.
        :param index2: Индекс правого элемента.
        :type index1: int
        :type index2: int

        """
        if _list[index1] < _list[index2]:
            _list[index1], _list[index2] = _list[index2], _list[index1]

    def sift_down(parent, limit):
        """
        Ищем максимальный среди родителя и потомков, и ставим его в корень.

        :param parent: Индекс родительского элемента.
        :param limit: Максимальное число элементов в куче. Ограничитель.
        :type parent: int
        :type limit: int

        """
        while True:
            child = parent * 2 + 2
            if child < limit:
                if _list[child] < _list[child - 1]:
                    child -= 1
                swap_items(parent, child)
                parent = child
            else:
                break

    length = len(_list)

    # Формирование первичной пирамиды.
    for index in range(int(length // 2) - 1, -1, -1):
        sift_down(index, length)

    # Окончательное упорядочение.
    for index in range(length - 1, 0, -1):
        swap_items(index, 0)
        sift_down(0, index)

    return _list


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(heap_sort(test_list))
