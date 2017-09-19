#!/usr/bin/python
# coding: utf8
"""
Сбалансированное Бинарное дерево поиска.

"""
from binary_three import BinaryThree


class Node(object):
    """
    Узел в дереве.

    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return "{}({})".format(self.value, self.height)


class AVLThree(BinaryThree):
    """
    Само дерево.

    """

    def add(self, value, recursive=True):
        """
        Добавление узла в дерево.

        :param value: Значение узла, которое надо добавить.
        :param recursive: Флаг, который указывает рекурсивно добавить или нет.
        :type value: object
        :type recursive: bool

        :return: Корень дерева.
        :rtype: Node

        """
        self.root = {True: self.__add_recursive, False: self.__add_not_recursive}[recursive](self.root, value)
        return self.root

    def __add_recursive(self, root, value):
        """
        Рекурсивное добавление листа в дерево.

        :param root: Корень дерева, в которое добавлем.
        :param value: Значение, которое добавляем.
        :type root: Node
        :type value: object

        :return: Node, который является корнем дерева.
        :rtype: Node

        """
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.__add_recursive(root.left, value)
        else:
            root.right = self.__add_recursive(root.right, value)

        return self.__balance(root)

    def __add_not_recursive(self, root, value):  # noqa
        """
        НЕ Рекурсивное добавление листа в дерево.

        :param root: Корень дерева, в которое добавлем.
        :param value: Значение, которое добавляем.
        :type root: Node
        :type value: object

        :return: Корень дерева.
        :rtype; Node

        """
        parents = []
        parent = None
        node = root
        while node is not None:
            parents.append(node)
            parent = node
            node = node.left if value < node.value else node.right

        new_node = Node(value)

        if parent is None:
            return new_node

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        parents.reverse()
        for index, _parent in enumerate(parents):
            parents[index] = self.__balance(_parent)

        return self.root

    def __delete_recursive(self, root, value):
        """
        Рекурсивное удаление узла из дерева.

        :param root: Корень дерева, из которого удаляем.
        :param value: Значение, которое надо удалить.
        :type root: Node
        :type value: object

        :return: Корень дерева.
        :rtype: Node or None

        """
        if root is None:
            return None

        if value < root.value:
            root.left = self.__delete_recursive(root.left, value)
            return self.__balance(root)
        elif value > root.value:
            root.right = self.__delete_recursive(root.right, value)
            return self.__balance(root)

        r, l = root.right, root.left
        if r is None:
            return l

        _min = self.min(r)
        _min.right = self.__remove_min(r)
        _min.left = l
        return self.__balance(_min)

    def __remove_min(self, root):
        """
        Удаление минимального узла из дерева с корнем в root.

        :param root: Корень дерева, в котором ищем.
        :type root: Node

        :return: Новый корень дерева.
        :rtype: Node

        """
        if root.left is None:
            return root.right
        root.left = self.__remove_min(root.left)
        return self.__balance(root)

    def __get_height(self, node=None):
        """
        Получить высоту ноды.

        :param node: Нода для получения или None.
        :type node: Node

        :return: Высоту ноды.
        :rtype: int

        """
        return node.height if node is not None else 0

    def __delta_height(self, node):
        """
        Возвращает разницу высот левого и правого поддерева.

        :param node: Нода, в которой получаем разницу высот.
        :type node: Node

        :return: Разницу высот.
        :rtype: int

        """
        return self.__get_height(node.right) - self.__get_height(node.left)

    def __fix_height(self, node):
        """
        Перерасчет высоты узла.

        :param node: Нода, с которой работаем.
        :type node: Node

        """
        pl = self.__get_height(node.left)
        pr = self.__get_height(node.right)
        node.height = (pl if pl > pr else pr) + 1

    def __rotate_right(self, node):
        """
        Правый поворот вокруг node.

        :param node: Нода, вокруг которой вертим.
        :type node: Node

        :return: Новая вершина на месте бывшего node.
        :rtype: Node

        """
        buf = node.left
        node.left = buf.right
        buf.right = node
        self.__fix_height(node)
        self.__fix_height(buf)
        return buf

    def __rotate_left(self, node):
        """
        Левый поворот вокргу node.

        :param node: Нода, вокруг которой вертим.
        :type node: Node

        :return: Новая вршина на месте бывшего node.
        :rtype: Node

        """
        buf = node.right
        node.right = buf.left
        buf.left = node
        self.__fix_height(node)
        self.__fix_height(buf)
        return buf

    def __balance(self, node):
        """
        Балансировка дерева с корнем в node.

        :param node: Корень дерева, которое надо отбалансировать.
        :type node: Node

        :return: Новый корень отбалансированного дерева.
        :rtype: Node

        """
        self.__fix_height(node)

        if self.__delta_height(node) == 2:
            if self.__delta_height(node.right) < 0:
                node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        if self.__delta_height(node) == -2:
            if self.__delta_height(node.left) > 0:
                node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        return node  # Балансировка не нужна.


if __name__ == "__main__":
    print("INIT BinaryThree(10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75)")
    three = AVLThree(10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75)
    three.cprint()
    print("{}{}".format("ADD RECURSIVE: 42", "-" * 50))
    three.add(42)
    three.cprint()
    print("{}{}".format("ADD NOT RECURSIVE: 43", "-" * 50))
    three.add(43, recursive=False)
    three.cprint()
    print("{}{}".format("SEARCH RECURSIVE AND NOT RECURSIVE: 75", "-" * 50))
    print(three.search(75))
    print(three.search(75, recursive=False))
    print("{}{}".format("DELETE RECURSIVE: 30", "-" * 50))
    three.delete(30)
    three.cprint()
    print("{}{}".format("DELETE RECURSIVE: 10", "-" * 50))
    three.delete(10)
    three.cprint()
    print("{}{}".format("SEARCH MIN IN THREE", "-" * 50))
    print(three.min().value)
    print("{}{}".format("SEARCH MAX IN THREE", "-" * 50))
    print(three.max().value)
    print("{}{}".format("EXTEND THREE VALUES: 43, 47, 53, 57, 11, 69, 28", "-" * 50))
    three.extend(43, 47, 53, 57, 11, 69, 28)
    three.cprint()
