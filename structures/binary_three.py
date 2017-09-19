#!/usr/bin/python
# coding: utf8
"""
Бинарное дерево поиска.

"""


class Node(object):
    """
    Узел в дереве.

    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryThree(object):
    """
    Класс нашего дерева, который реализует все функции структуры данных.

    """
    def __init__(self, *args):
        args = list(args)
        self.root = None

        if args:
            self.add(args.pop(0))

        for val in args:
            self.add(val)

    def __str__(self):
        return "{}()".format(
            self.__class__.__name__,
        )

    def __repr__(self):
        return self.__str__()

    def cprint(self, node=None, level=0, separator="-"):
        """
        Рекурсивная печать дерева в консоль.

        :param node: Текущая нода, которую печатаем.
        :param level: Текущий уровень.
        :param separator: Разделитель ветвей.
        :type node: Node
        :type level: int
        :type separator: str

        """
        if level == 0:
            node = self.root

        if node is None:
            return

        if node.left is not None:
            self.cprint(node.left, level + 1, separator)

        print("{} {}".format(separator * level, node.value))

        if node.right is not None:
            self.cprint(node.right, level + 1, separator)

    def min(self, root=None):
        """
        Возвращает минимальное значение в дереве с корнем в root если root указано, либо в self.root.

        :param root: Корень дерева, в котором ищем минимум.
        :type root: Node

        :return: Минимальное значение.
        :rtype: Node

        """
        root = root if root is not None else self.root
        if root is None:
            return None

        while root.left is not None:
            root = root.left

        return root

    def max(self, root=None):
        """
        Возвращает максимальное значение в дереве с корнем в root если root указано, либо в self.root.

        :param root: Корень дерева, в котором ищем максимум.
        :type root: Node

        :return: Максимальное значение.
        :rtype: Node

        """
        root = root if root is not None else self.root
        if root is None:
            return None

        while root.right is not None:
            root = root.right

        return root

    def extend(self, *values):
        """
        Добавлет в дерево все значение values.

        :param values: Значения дл добавления.

        """
        for val in values:
            self.add(val)

    def __replace_child(self, parent, old, new):
        """
        Заменяет у узла parent значение потомка old на потомка new.
        Если parent пустой, тогда new ставим в корень.

        :param parent: Родительский узел.
        :param old: Старый улез.
        :param new: Новый узел.
        :type parent: Node
        :type old: Node
        :type new: Node

        """
        if parent is None:
            self.root = new
        elif parent.left == old:
            parent.left = new
        elif parent.right == old:
            parent.right = new

    def search(self, value, recursive=True):
        """
        Поиск в дереве. По дефолту используется рекурсивный поиск.
        Можно запустить нерекурсивный опусти флаг recursive.

        :param value: Значение которое ищем.
        :param recursive: Флаг, указывающий какой поиск использовать. Рекурсивный или нет.
        :type value: object
        :type recursive: bool

        :return: Найденный узел или ничего.
        :rtype; Node or None

        """
        return {True: self.__search_recursive, False: self.__search_not_recursive}[recursive](self.root, value)

    def __search_recursive(self, root, value):
        """
        Рекурсивный поиск value в дереве с корнем node.

        :param root: Корень дерева, в котором ищем сейчас.
        :param value: Искомое знаечние.
        :type root: Node
        :type value: object

        :return: Найденный узел иои ничего.
        :rtype: Node ot None

        """
        if root is None or root.value == value:
            return value
        elif value < root.value:
            return self.__search_recursive(root.left, value)
        else:
            return self.__search_recursive(root.right, value)

    def __search_not_recursive(self, root, value):
        """
        НЕ рекурсивный поиск value в дереве с корнем node.

        :param root: Корень дерева, в котором ищем сейчас.
        :param value: Искомое знаечние.
        :type root: Node
        :type value: object

        :return: Найденный узел или ничего.
        :rtype: Node or None

        """
        node = root
        while node is not None:
            if value == node.value:
                return node
            node = node.left if value < node.value else node.right

        return None

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

        return root

    def __add_not_recursive(self, root, value):
        """
        НЕ Рекурсивное добавление листа в дерево.

        :param root: Корень дерева, в которое добавлем.
        :param value: Значение, которое добавляем.
        :type root: Node
        :type value: object

        :return: Корень дерева.
        :rtype; Node

        """
        parent = None
        node = root
        while node is not None:
            parent = node
            node = node.left if value < node.value else node.right

        new_node = Node(value)

        if parent is None:
            return new_node

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        return self.root

    def delete(self, value, recursive=True):
        """
        Удаление узла из дерева.

        :param value: Значение, которое надо удалить.
        :param recursive: Флаг, который указывает рекурсивно удалить или нет.
        :type value: object
        :type recursive: bool

        :return: Корень дерева.
        :rtype: Node or None

        """
        self.root = {True: self.__delete_recursive, False: self.__delete_not_recursive}[recursive](self.root, value)
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
            return root
        elif value > root.value:
            root.right = self.__delete_recursive(root.right, value)
            return root

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_val = self.min(root.right).value
            root.value = min_val
            root.right = self.__delete_recursive(root.right, min_val)
            return root

    def __delete_not_recursive(self, root, value):
        """
        НЕ Рекурсивное удаление узла из дерева.

        :param root: Корень дерева, из которого удаляем.
        :param value: Значение, которое надо удалить.
        :type root: Node
        :type value: object

        :return: Корень дерева.
        :rtype: Node or None

        """
        parent = None
        root = root if isinstance(root, Node) else self.root

        while True:
            if root is None:
                return
            if value < root.value:
                parent = root
                root = root.left
            elif value > root.value:
                parent = root
                root = root.right
            else:
                break

        result = None

        if root.left is None:
            result = root.right
        elif root.right is None:
            result = root.left
        else:
            min_node_parent = root
            min_node = root.right
            while min_node.lef is not None:
                min_node_parent = min_node
                min_node = min_node.left

            result = root
            root.value = min_node.value
            self.__replace_child(min_node_parent, min_node, min_node.right)

        self.__replace_child(parent, root, result)

        return self.root


if __name__ == "__main__":
    print("INIT BinaryThree(10, 15, 5, 13, 17, 12, 14, 16, 18, 2, 7, 1, 3, 6, 9)")
    three = BinaryThree(10, 15, 5, 13, 17, 12, 14, 16, 18, 2, 7, 1, 3, 6, 9)
    three.cprint()
    print("{}{}".format("ADD RECURSIVE: 25", "-" * 50))
    three.add(25)
    three.cprint()
    print("{}{}".format("ADD NOT RECURSIVE: 11", "-" * 50))
    three.add(11, recursive=False)
    three.cprint()
    print("{}{}".format("SEARCH RECURSIVE AND NOT RECURSIVE: 11", "-" * 50))
    print(three.search(11))
    print(three.search(11, recursive=False))
    print("{}{}".format("DELETE RECURSIVE: 11", "-" * 50))
    three.delete(11)
    three.cprint()
    print("{}{}".format("DELETE NOT RECURSIVE: 18", "-" * 50))
    three.delete(18, recursive=False)
    three.cprint()
    print("{}{}".format("DELETE RECURSIVE: 10", "-" * 50))
    three.delete(10)
    three.cprint()
    print("{}{}".format("SEARCH MIN IN THREE", "-" * 50))
    print(three.min().value)
    print("{}{}".format("SEARCH MAX IN THREE", "-" * 50))
    print(three.max().value)
    print("{}{}".format("EXTEND THREE VALUES: 50, 45, 55, 43, 47, 53, 57", "-" * 50))
    three.extend(50, 45, 55, 43, 47, 53, 57)
    three.cprint()
