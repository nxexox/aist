#!/usr/bin/python
# coding: utf8
"""
Структура данных Очередь.

"""


class Queue(object):
    def __init__(self, value=None):
        self.__queue = list()
        if isinstance(value, list):
            self.__queue.extend(value)
        elif value is not None:
            self.__queue.append(value)

    def push(self, value):
        """
        Добавить элемент.

        :param value: Элемент.
        :type value: object

        """
        self.__queue.append(value)

    def pop(self):
        """
        Достает элемент из стэка и удаляет его.

        :return: Элемент или None
        :rtype: object or None

        """
        try:
            return self.__queue.pop(0)
        except IndexError:
            return None

    def get(self):
        """
        Просто достает элемент из стэка.

        :return: Элемент или None
        :rtype: object or None

        """
        try:
            return self.__queue[0]
        except IndexError:
            return None

    def is_empty(self):
        """
        Проверяет пустой ли стэк.

        :return: Результат проверки.
        :rtype: bool

        """
        return bool(len(self.__queue))

if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    while not queue.is_empty():
        print(queue.pop())

        queue = Queue([1, 2, 3, 56, 24, 124])
    while not queue.is_empty():
        print(queue.pop())
