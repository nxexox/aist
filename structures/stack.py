#!/usr/bin/python
# coding: utf8
"""
Структура данных СТЭК.

"""


class Stack(object):
    def __init__(self, value=None):
        self.__stack = list()
        if isinstance(value, list):
            self.__stack.extend(value)
        elif value is not None:
            self.__stack.append(value)

    def push(self, value):
        """
        Добавить элемент.

        :param value: Элемент.
        :type value: object

        """
        self.__stack.append(value)

    def pop(self):
        """
        Достает элемент из стэка и удаляет его.

        :return: Элемент или None
        :rtype: object or None

        """
        try:
            return self.__stack.pop()
        except IndexError:
            return None

    def get(self):
        """
        Просто достает элемент из стэка.

        :return: Элемент или None
        :rtype: object or None

        """
        try:
            return self.__stack[len(self.__stack) - 1]
        except IndexError:
            return None

    def is_empty(self):
        """
        Проверяет пустой ли стэк.

        :return: Результат проверки.
        :rtype: bool

        """
        return bool(len(self.__stack))

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    while not stack.is_empty():
        print(stack.pop())

    stack = Stack([1, 2, 3, 56, 24, 124])
    while not stack.is_empty():
        print(stack.pop())
