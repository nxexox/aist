#!/usr/bin/python
# coding: utf8
"""
Структура данных SET.

"""


class Set(object):
    """
    Множество.
    Мтетоды:
         - - Разность множеств
         + - Объединение множеств
         / - Пересечение множеств
         // - Семмитричная разность множеств.
    """
    def __init__(self, value=None):
        self.__set = list()
        if isinstance(value, list):
            self.__set.extend(value)
        elif value is not None:
            self.__set.append(value)

    def __str__(self):
        return "(" + ", ".join(map(str, self.__set)) + ")"

    def __repr__(self):
        return "Set([" + ", ".join(map(str, self.__set)) + "])"

    def append(self, value):
        """
        Добавить элемент.

        :param value: Элемент.
        :type value: object

        """
        self.__set.append(value)

    def get(self, index):
        """
        Просто достает элемент из стэка.

        :param index: Индекс элемента для получения
        :rtype: int

        :return: Элемент или None
        :rtype: object or None

        """
        try:
            return self.__set[index]
        except IndexError:
            return None

    def is_empty(self):
        """
        Проверяет пустой ли стэк.

        :return: Результат проверки.
        :rtype: bool

        """
        return bool(len(self.__set))

    def search(self, value):
        """
        Поиск во множестве.

        :param value: Значние которое ищем.
        :type value: object

        :return: Есть ли такое значение во множестве.
        :rtype: bool

        """
        return value in self.__set

    def __add__(self, other):
        """ Объединение. """
        _set = Set(self.__set)
        for i in other:
            if not self.search(i):
                _set.append(i)

        return _set

    def __sub__(self, other):
        """ Разность. """
        _set = Set()
        for i in self:
            if not other.search(i):
                _set.append(i)

        return _set

    def __truediv__(self, other):
        """ Пересечение множеств. """
        _set = Set()
        for i in other:
            if self.search(i):
                _set.append(i)

        return _set

    def __floordiv__(self, other):
        """ Семмитричное пересечение множеств. """
        _set = Set()
        for i in self:
            if not other.search(i):
                _set.append(i)
        for i in other:
            if not self.search(i):
                _set.append(i)

        return _set

    def __div__(self, other):
        return self.__truediv__(other)

    def __iter__(self):
        for i in self.__set:
            yield i

if __name__ == "__main__":
    set_one = Set([1, 2, 3, 4, 5, 6])
    set_two = Set([5, 6, 7, 8, 9, 10])
    print("{} - {} = {}".format(set_one, set_two, set_one - set_two))
    print("{} + {} = {}".format(set_one, set_two, set_one + set_two))
    print("{} / {} = {}".format(set_one, set_two, set_one / set_two))
    print("{} // {} = {}".format(set_one, set_two, set_one // set_two))
