#!/usr/bin/python
# coding: utf8
"""
Самые базовые алгоритмы поиска.

"""

from .base_search import base_search
from .kmp import kmp_search
from .bm import bm_search


if __name__ == "__main__":
    needle = "test"
    haystack = "teskiiteshfuesta,mvvmtestkl;lkgggoo87testnmn,,mtestnjhhkkteskjlktestkljkgljh"
    print(base_search(needle, haystack))  # Прямой поиск.
    print(kmp_search(needle, haystack))  # КМП.
