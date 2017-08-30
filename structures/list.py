#!/usr/bin/python
# coding: utf8
"""
Структура данных Двунаправленный связный список.

"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class List(object):
    def __init__(self, value=None):
        self.header = None if value is None else Node(value)

    def search(self, value):
        """
        Поиск элемента.

        :param value: Значени для поиска
        :type value: object

        :return: Найденный объект.
        :rtype: object

        """
        start = self.header
        while start:
            if start.value == value:
                return start
            start = start.right

        return None

    def append(self, value):
        """
        Добавление в список.

        :param value: Значение которое надо доавить
        :type value: object

        """
        end = self.header
        while end.right:
            end = end.right
        end.right = Node(value)
        end.right.left = end

    def remove(self, value):
        """
        Удаление из список.

        :param value: Значение которое надо удалить
        :type value: object

        """
        el = self.search(value)
        if el is None:
            return None
        el.left.right = el.right
        del el
        return True

    def __iter__(self):
        el = self.header
        while el:
            yield el
            el = el.right

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

if __name__ == "__main__":
    _list = List(1)
    _list.append(3)
    _list.append(5)
    _list.append(7)
    _list.append(11)
    print(_list)
    print(_list.search(10), _list.search(11))
    _list.remove(4)
    _list.remove(3)
    print(_list)
    _list.remove(7)
    print(_list)
