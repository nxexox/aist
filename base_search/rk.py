#!/usr/bin/python
# coding: utf8
"""
Рабина-Карпа(РК)
O((N - M + 1) * M)
"""


def circular_hash(old_string, len_str, new_char=None, old_hash=None):
    """
    Кольцевая хэш функция, по сумме произведений кодов символа на простое основание в степени.

    :param old_string: Строка, для которой вычислен хэш.
    :param len_str: Длина строки, для которой высчитываем значение функции.
    :param new_char: Последний символ новой строки.
    :param old_hash: Старый хэш.
    :type old_string: str
    :type len_str: int
    :type new_char: str
    :type old_hash: int

    :return: Вычисленный хэш.
    :rtype: int

    """
    base = 59
    if old_hash is None:
        # Считаем хэш впервые.
        return sum([ord(el) * (base ** (len_str - index - 1)) for index, el in enumerate(old_string)])

    return (old_hash - ord(old_string[0]) * (base ** (len_str - 1))) * base + ord(new_char)


def rk_search(needle, haystack):
    """
    Поиск КМП.
    Возвращает индекс найденной строки либо None, если строка не найдена.

    :param needle: Искомая подстрока.
    :param haystack: Строка, в которой ищем.
    :type needle: str
    :type haystack: str

    :return: Индекс первого найденного вхождения.
    :rtype: int

    """
    len_needle = len(needle)
    len_haystack = len(haystack)
    hash_needle = circular_hash(needle, len_needle)
    hash_haystack = circular_hash(haystack[:len_needle], len_needle)

    for i in range(len_haystack - len_needle + 1):
        # Если хэш совпал, проверяем строку.
        if hash_haystack == hash_needle:
            result = 0
            for j in range(len_needle):
                if needle[j] == haystack[i + j]:
                    result += 1
            if result == len_needle:
                return i
        # Если не совпал, тогда пересчитываем хэш и идем дальше.
        hash_haystack = circular_hash(
            haystack[i: i + len_needle],
            len_needle,
            haystack[i + len_needle],
            hash_haystack
        )

    return None


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuestamvvmtestkllkgggootestnmnmtestnjhhkkteskjlktestkljkgljh"
    hash_test = "ababcaba"
    print(circular_hash(hash_test, len(hash_test)))  # Хэш функция.
    print(rk_search(needle, haystack))  # Поиск РК.

