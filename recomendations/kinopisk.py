#!/usr/bin/python
# coding: utf-8
"""
Парсит данные по оценкам с кинопоиска.
Тащит ID, Title, Rating, и все оценки по фильму.

ВАЖНО!!! КНОПОИСК БЛОЧИТ, ТАК ЧТО БОЛЬШЕ 20-100 фильмов за раз не собрать.
НАДО ЛИБО ПРИДУМЫВАТЬ ЧТО ТО, ЛИБО ОЧЕРЕДЯМИ ДЕЛАТЬ.

"""
import json
import os
import sys
import logging
import random
import datetime
import requests
from xml.etree import ElementTree as ET


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Parser(object):
    """
    Парсер кинопоиска.
    Предоставляет методы:
        * get_url(user_id) - Формирует и возвращает URL для конкретного пользователя, что бы собрать все его оценки.
        * get_user_data(user_id) - Формирует и возвращает все оценки конкретного пользователя.
        * save(file_name, data) - Сохраняет словарь data в файл по пусти с именем file_name.
        * main_while(max_count_except) - Собирает и сохраняет данные по нескольким пользователям.
            max_count_except - Максимальное кол-во подряд идущих ошибок, для отстановки сбора.
            Например нас залочили.
            По дефолту равен 10.

    Конструктор принимает конфигурационные данные:
        * star_id - ID пользователя, с которого начинаем сбор. По дефолту равен 2.
        * end_id - ID пользователя, на котором останавливаем сбор. По дефолту равен 5000.
        * step - Шаг между пользователями. ПО дефолту равен 1.
        * file_path - Путь до папки, куда сохранить результаты сбора. По дефолту сохраняет в папку со скриптом.

    Самый простой пример использования:
    parser = Parser(2, 1000, file_path="/home/user/projects/aist/recomendations/datasets/")
    result = parser.main_while()
    # На этом этапе у нас появится файл с результами.
    # Так же результаты будут возвращены в виде словаря в result.

    """
    def __init__(self, start_id=None, end_id=None, step=1, file_path=None):
        """
        Ставим нужные параметры по дефолту.

        :param start_id: ID с которого начинаем.
        :param end_id: ID которым заканчиваем.
        :param step: Шаг, с которым работаем.
        :param file_path: Путь до файла, в который сохраняем.
        :type start_id: int
        :type end_id: int
        :type step: int
        :type file_path: str

        """
        self.__start_id = start_id if start_id and start_id > 1 else 2
        self.__end_id = end_id if end_id and end_id > 1 else 5000
        self.__step = step if step and step > 0 else 1
        self.__revision = 0.14538243807779217  # Ревизия конкретного пользователя.
        self.__revision_step = 1E-16  # Шаг ревизии
        self.__url_template = "https://www.kinopoisk.ru/graph_data/last_vote_data/{short_id}/last_vote_{user_id}__all.xml?{revision}"
        self.__file_path = file_path

    @property
    def revision(self):
        """
        Возвращает текущую ревизию. Каждый раз разную.

        :return: Ревизия для запроса.
        :rtype: str

        """
        if random.getrandbits(1):
            self.__revision += self.__revision_step
        else:
            self.__revision -= self.__revision_step
        return str(self.__revision)

    def get_url(self, user_id):
        """
        Формирует ссылку на парсинг инфы для конкретного юзера.

        :param user_id: ID пользователя.
        :type user_id: int

        :return: Готовая ссылка.
        :rtype: str

        """
        if user_id > 999:
            data = {"short_id": str(user_id)[-3:], "user_id": user_id, "revision": self.revision}
        else:
            data = {"short_id": "{:03d}".format(user_id), "user_id": user_id, "revision": self.revision}
        return self.__url_template.format(**data)

    def get_user_data(self, user_id):
        """
        Достает инфу по конкретному пользователю.

        :param user_id: ID пользователя, по которому пробуем достать.
        :type: int

        :return: Словарь с данными по пользователю.
        :rtype: dict

        """
        result = {}
        url = self.get_url(user_id)
        response = requests.get(url)
        if response.status_code != 200:
            logger.error("Ошибка ответа сети. USER: {}. STATUS_CODE: {}. URL: {}".format(
                user_id, response.status_code, self.get_url(user_id)
            ))
            return {}

        if response.headers.get("Content-Type", "text/html") != "text/xml":
            logger.error("Неверный Content-Type. USER: {}. URL: {}. Headers: {}".format(
                user_id, url, response.headers
            ))
            return {}

        tree = ET.fromstring(response.content)
        for graph in tree.iter("graph"):
            for value in graph.iter("value"):
                try:
                    film_id = int(value.attrib["url"].split("/")[2])
                    result[film_id] = {
                        "id": film_id,
                        "title": value.attrib["description"],
                        "rating": int(value.text)
                    }
                except Exception as e:
                    logger.error("Ошибка парсинга строки. USER: {}. Подробнее: {}".format(user_id, e))

        return result

    def main_while(self, max_count_except=10):
        """
        Основной цикл по всем пользователям. Всем критикам.

        :param max_count_except: Максимальное кол-во ошибок подряд.
        :type max_count_except: int

        :return: Кол-во критиков, которые были сохранены. Так-же, кол-во фильмов которые в итоге встретились.
        :rtype: dict

        """
        __count_except = 0
        critics = {}
        films = {}
        __count_iters = (self.__end_id - self.__start_id) / self.__step
        for user_id in range(self.__start_id, self.__end_id, self.__step):
            # Выводим прогресс.
            self.__print_progress_bar(user_id - self.__start_id, int(__count_iters) - 1)
            # Если достигли лимита ошибок, дальше нет смысла. Нас забанили. Пишем и останавливаемся.
            if __count_except >= max_count_except:
                logger.error("Достигли лимита ошибок. "
                             "Спарсено пользователей: {}. "
                             "Последний удачно спарсенный: {}. "
                             "Фильмов найдено: {}. "
                             "Пишем все в файл.".format(len(critics), max(critics.keys()), len(films)))
                break

            # Достаем данные.
            try:
                user_ratings = self.get_user_data(user_id)
            except Exception as e:
                logger.error("Произошла неизвестная ошибка. USER: {}. Подробнее: {}".format(
                    user_id, e
                ))
                user_ratings = {}

            # Если данные не удалось достать, увеличиваем кол-во ошибок.
            if user_ratings == {}:
                __count_except += 1
                continue

            # Пополняем список фильмов.
            for key, val in user_ratings.items():
                films[key] = val.get("title")

            __count_except = 0
            critics[user_id] = user_ratings

        file_name_critics = self.__get_file_path(prefix_file="critics-")
        file_name_films = self.__get_file_path(prefix_file="films-")
        print("Сбор данных завершен. Пишем в файл по имени: {}, {}. Критиков спарсено: {}. "
              "Фильмов найдено: {}. Прогнозируемый размер файла критиков: {}. "
              "Прогнозируемый размер файла фильмов: {}.".format(
                  file_name_critics, file_name_films, len(critics), len(films),
                  sys.getsizeof(critics), sys.getsizeof(films)
              )
        )
        self.save(file_name_critics, critics)
        self.save(file_name_films, films)
        return critics

    def __print_progress_bar(self, iteration, total, length=100, fill='█'):
        """
        Выводит прогресс бар в консоли.

        :param iteration: Текущая итерация.
        :param total: Всего должно быть итераций.
        :param length: Длина прогресс бара в символах.
        :param fill: Символ, заполняющий прогресс бар.
        :type iteration: int
        :type total: int
        :type length: int
        :type fill: str

        """
        percent = ("{0:." + "4" + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + "-" * (length - filled_length)
        print("\rПрогресс парсинга: |%s| %s%% Завершено." % (bar, percent), end="\r")
        if iteration == total:
            print()

    def __get_file_path(self, prefix_file=None):
        """
        Формирует и возвращает путь до файла, включая название файла.

        :param prefix_file: Префикс для названия файла.
        :type prefix_file: str

        :return: Итоговый путь для сохранения файла.
        :rtype: str

        """
        file_name = prefix_file if prefix_file else ""
        file_name += datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f.json")
        if self.__file_path:
            return os.path.join(self.__file_path, file_name)
        return file_name

    def save(self, file_name, data):
        """
        Пишет результаты в файл.

        :param file_name: Название файла, в который пишем.
        :param data: Словарь, который записать.
        :type file_name: str
        :type data: dict

        """
        with open(file_name, "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    parser = Parser(2, 10000000, file_path="datasets")
    result = parser.main_while(10000)
