#!/usr/bin/python
# coding: utf8
"""
Коллабороторная фильтрация. Простой способ выработки рекомендаций.

Собирает людей, которым нравится то же что и вам. Потом берем то что им нравится, но что я не видел,
группируем и получаем рекомендации.

Рассматриваем коллаборативную фильтрацию на основе рекомендаций фильмов.
Поиск похожих фильмов, которые я еще не видел.

С помощью скрипта recomendations/kinopoik.py
Можно загрузить какое то кол-во реальныз оцерок реальных фильмов от реальых людей кинопоиска
Что бы попробовать составить реальную систему рекомендаций, хотя бы для себя.

"""
from math import sqrt
import json

# Пример словаря критиков, с которым работают функции.
critics = {
    "Мои оценки": {
        "Фильм 1": 2.5,
        "Фильм 2": 3.5,
        "Фильм 3": 3.0,
        "Фильм 4": 3.5,
        "Фильм 5": 2.5,
        "Фильм 6": 3.0
    }, 
    "Оценки какого то парня": {
        "Фильм 1": 4.9,
        "Фильм 15": 2.2
    }
}


def load_critics(file_path):
    """
    Загружает критиков из файла и превращает в словарь.

    :param file_path: Путь до датасета.
    :type file_path: str

    :return: Словарь с критиками и оценками.
    :rtype: dict

    """
    with open(file_path, "r") as f:
        return json .load(f, encoding="utf-8")


def sim_distance_euclidean(critics, person_one, person_two):
    """
    Возвращает оценку подобия person1 и person2 на основе евклидова расстояния.

    sqrt( ( (x1 - x2) ^ 2 + (y1 - y2) ^ 2) )

    :param critics: Список всех критиков с их оценками фильмов.
    :param person_one: Имя критика номер один.
    :param person_two: Имя критика номер два.

    :return: Просчитанное расстояние между двумя критиками на основе их оценок.
    :rtype: float

    """
    # Получить список предметов, оцененных обоими
    si = {
        item: 1 for item in critics[person_one].keys() if item in critics[person_two]
    }

    # Если нет ни одной общей оценки, возвращаем 0.
    if len(si) == 0:
        return 0

    # Сложить квадраты разностей
    sum_of_squares = sum([
        pow(critics[person_one][item] - critics[person_two][item], 2)  # Высчитываем евклидово расстояние.
        for item in critics[person_one] if item in critics[person_two]
    ])

    # Что бы функция возвращала значение по возрастанию похожести, приходиться инвертировать ее.
    return 1 / (1 + sum_of_squares)


def sim_distance_pearson(critics, person_one, person_two):
    """
    Возвращает оценку подобия person1 и person2 на основе кореляции пирсона.

    Возвращает от -1 до 1.
    1 Значит оценки двух людей в точности одинаковые.
    -1 Значит между людьми ничего общего.

    :param critics: Словарь всех критиков.
    :param person_one: Имя критика номер один.
    :param person_two: имя критика номер два.

    :return: Просчитанное значение между двумя критиками на основу их оценок.
    :rtype: float

    """
    # Достаем оценки двух критиков.
    si = {item: 1 for item in critics[person_one].keys() if item in critics[person_two]}
    n = len(si)

    # Если нет общих оценок, возвращаем 0.
    if n == 0:
        return 0

    # Вычисляем сумму всех предпочтений.
    sum_one = sum([critics[person_one][it] for it in si])
    sum_two = sum([critics[person_two][it] for it in si])

    # Вычисляем суммы квадратов.
    sum_one_sqr = sum([pow(critics[person_one][it], 2) for it in si])
    sum_two_sqr = sum([pow(critics[person_two][it], 2) for it in si])

    # Вычисляем сумму произведений.
    sum_op = sum([critics[person_one][it] * critics[person_two][it] for it in si])

    # Коэфициент Пирсона.
    num = sum_op - (sum_one * sum_two / n)
    den = sqrt((sum_one_sqr - pow(sum_one, 2) / n) * (sum_two_sqr - pow(sum_two, 2) / n))

    if den == 0:
        return 0

    return num / den


def top_matches(critics, person, n=5, similarity=sim_distance_pearson):
    """
    Возвращает список наилучших соответствий для человека из словаря critics.
    Количество результатов в списке и функция подобия – необязательные параметры.
    Самых близких ко мне по духу, критиков.

    :param critics: Список критиков, по которому работаем.
    :param person: Имя критика, для которого подбираем.
    :param n: Кол-во наилучших соотвествий.
    :param similarity: Объект функции, которая вычисляет расстояния.

    :return: Список наилучших соотвествий.
    :rtype: list

    """
    scores = [
        (similarity(critics, person, other), other)
        for other in critics if other != person
    ]
    # Отсортировать список по убыванию оценок.
    scores.sort()
    scores.reverse()
    return scores[0:n]


def get_recommendations(critics, person, similarity=sim_distance_pearson):
    """
    Получить рекомендации для заданного человека, пользуясь взвешенным средним
    оценок, данных всеми остальными пользователями

    :param critics: Словарь критиков, с которыми работаем.
    :param person: Имя человека, для которого хотим сделать рекомендации.
    :param similarity: Функция вычисления расстояния.

    :return: Список фильмов, с максимальным рангом рекомендации.
    :rtype: list

    """
    totals = {}
    sim_sums = {}
    for other in critics:
        # Сравнивать меня с собой же не нужно.
        if other == person:
            continue
        sim = similarity(critics, person, other)

        # Игнорируем нулевые и отрицательные оценки.
        if sim <= 0:
            continue

        for item in critics[other]:
            # Оцениваем только фильмы, которые я еще не смотрел.
            if item not in critics[person] or critics[person][item] == 0:
                # Коэффициент подобия * Оценка.
                totals.setdefault(item, 0)
                totals[item] += critics[other][item] * sim
                # Сумма коэффициентов подобия.
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    # Создать нормализованный список.
    rankings = [
        (total / sim_sums[item], item)
        for item, total in totals.items()
    ]
    # Вернуть отсортированный список.
    rankings.sort()
    rankings.reverse()
    return rankings


if __name__ == "__main__":
    import random
    import time
    source_critics = load_critics("datasets/critics-06-10-2017-17-11-20-213655.json")  # Грузим критиков из датасета.
    source_films = load_critics("datasets/films-06-10-2017-17-11-20-213740.json")  # Грузим фильмы.
    # Теперь надо привести словарь критиков к нормальному формату.
    critics = {
        critic: {
            film_id: val["rating"] for film_id, val in films.items()
            if "rating" in val
        }
        for critic, films in source_critics.items()
    }

    # Достаем случайного критика, и выдаем за себя.
    i = list(critics.keys())[random.randint(0, len(critics.keys()) - 1)]
    # Для тестирования функций расстояния, мы просто берем еще одного случайного критика.
    other = list(critics.keys())[random.randint(0, len(critics.keys()) - 1)]

    # Само тестирование.
    # Евклидово расстояние.
    tic = time.time()
    euclidean = sim_distance_euclidean(critics, i, other)
    tac = time.time()
    print("Euclidean: ", euclidean, " Time spent: ", tac - tic)

    # Расстояние Пирсона.
    tic = time.time()
    pearson = sim_distance_pearson(critics, i, other)
    tac = time.time()
    print("Pearson: ", pearson, " Time spent: ", tac - tic)

    # Похожие критики.
    tic = time.time()
    matches = top_matches(critics, i)
    tac = time.time()
    print("Top Matches: ", matches, " Time spent: ", tac - tic)

    # Рекомендации фильмов, которые я еще не смотрел.
    tic = time.time()
    recommendations = get_recommendations(critics, i)
    tac = time.time()
    print("Get Recomendation: ", recommendations[:50], " Time spent: ", tac - tic)
    # Теперь для пользователя, преобразуем ID фильмов из рекомендации в названия фильмов.
    print("Recomendation on names: ", [source_films[i[1]] for i in recommendations[:50]])
