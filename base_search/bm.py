#!/usr/bin/python
# coding: utf8
"""
Бойера-Мура-Хорспула(БМХ)
О((N - M + 1) * M + p), где p – мощность алфавита.
Сама проверка идем справа на лево.

"""


def stop_table(needle):
    """
    Строим стоп таблицу. Важно, последний символ не учитывается.

    :param needle: Строка для построения.
    :type needle: str

    :return: Словарь стоп слов. Ключ это символ строки, значение его значение.

    """
    result = {}
    len_needle = len(needle)

    for i in range(len_needle - 1):
        result[needle[i]] = len_needle - i - 1

    return result


def bm_search(needle, haystack):
    """
    Поиск БМ.
    Возвращает индекс найденной строки либо None, если строка не найдена.

    :param needle: Искомая подстрока.
    :param haystack: Строка, в которой ищем.
    :type needle: str
    :type haystack: str

    :return: Индекс первого найденного вхождения.
    :rtype: int

    """
    _stop_table = stop_table(needle)
    len_needle = len(needle)  # Длина искомой строки.
    i = len_needle - 1  # Главный счетчик.
    result = None

    while i < len(haystack) and result is None:  # Идем по главной строке.

        j = 0  # Внутренний счетчик поиска.
        while j < len_needle:  # Пробуем найти подстроку, идя с конца.
            if haystack[i - j] != needle[len_needle - j - 1]:
                break
            j += 1

        # Теперь смотрим, если нашли, закончили поиск. Иначе смотрим на сколько смещаться.
        if j == len_needle:
            result = i - j
        elif j != 0:
            i += 1
        else:
            offset = _stop_table.get(haystack[i - j], len_needle)
            i += offset

    return result


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuestamvvmtestkllkgggootestnmnmtestnjhhkkteskjlktestkljkgljh"
    print(stop_table(needle))  # Строим стоп таблицу.
    print(bm_search(needle, haystack))  # Поиск БМ.
