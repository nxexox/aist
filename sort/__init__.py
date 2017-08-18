#!/usr/bin/python
# coding: utf8

from .comb_sort import comb_sort
from .heap_sort import heap_sort
from .insert_sort import insert_sort
from .quick_sort import quick_sort
from .radix_sort import radix_sort
from .shell_sort import shell_sort


if __name__ == "__main__":
    test_list = [12, 68, 213, 1, 59, 394, 43, 12, 645, 324, 98, 999, 998]
    print(insert_sort(test_list))  # Сортировка вставками.
    print(radix_sort(test_list))  # Поразрядная сортировка.
    print(comb_sort(test_list))  # Сортировка расческой.
    print(shell_sort(test_list))  # Сортировка Шелла.
    print(quick_sort(test_list))  # Быстрая сортировка.
    print(heap_sort(test_list))  # Пирамидальная сортировка.
