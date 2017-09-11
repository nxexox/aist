# coding: utf8
import math

class Node(object):
    """
    Нода для сбаллансированного бинарного дерева.
    """

    value = None
    left = None
    right = None
    level = 0

    def __init__(self, value, left=None, right=None, level=0):
        """Инициализируем ноду, добавляем правый левый элемент"""

        self.value = value
        self.left = left if left else None
        self.right = right if right else None
        self.level = level

    def __str__(self):
        """Пишем строковое представление ноды"""

        return 'Node(value: {}, level: {}, l:{}, r:{})\n'.format(self.value, self.level, 
            self.left.value if self.left else '', self.right.value if self.right else '')

    def _to_tree(self):
        """Рекурсивно рендерим ноду в дерево-подобное представление"""

        return '{root:_>{level}}\n{left:_>{level}}{right:_>{level}}'.format(
            root = self.value, level = self.level * 4,
            left = self.left._to_tree() if self.left else '{:_>{}}\n'.format('#l', self.level * 4 + 4),
            right = self.right._to_tree() if self.right else '{:_>{}}\n'.format('#r', self.level * 4 + 4))


    def _fix_levels(self):
        """
        Лечим поломанные указатели уровней ноды. Рекурсивно пробегаем все дерево, 
        считаем уровни вручную и подставляем правильные значения
        """

        if self.left:
            if self.left.level is not self.level + 1:
                self.left.level = self.level + 1
            self.left = self.left._fix_levels()
        if self.right:
            if self.right.level is not self.level + 1:
                self.right.level = self.level + 1
            self.right = self.right._fix_levels()
        
        return self

    def _swap_left(self):
        """Левый поворот"""

        if not self.right:
            return

        right = self.right.right if self.right.right else None
        value = self.right.value

        self.left = Node(
            self.value, 
            right=self.right.left if self.right and self.right.left else None, 
            left=self.left if self.left else None, 
            level=self.level+1)

        self.right = right
        self.value = value
        self._fix_levels()

    def _swap_right(self):
        """Правый поворот"""

        if not self.left:
            return

        left = self.left.left if self.left.left else None
        value = self.left.value
        
        self.right = Node(
            self.value, 
            right=self.right if self.right else None, 
            left=self.left.right if self.left and self.left.right else None, 
            level=self.level+1)

        self.left = left
        self.value = value
        self._fix_levels()

    def _swap_right_left(self):
        """Правый\левый поворот"""

        self.right._swap_right()
        self._swap_left()

    def _swap_left_right(self):
        """Левый\правый поворот"""

        self.left._swap_left()
        self._swap_right()

    def balance(self):
        """Балансировка дерева по ноде"""

        # Лечим перепутанные уровни
        self._fix_levels()

        # Пытаемся понять, нужен ли нам двойной поворот или хватит одного. Определяем по разницы длинн веток
        double_swap = math.fabs(self.right.depth() if self.right else 0) \
                        < math.fabs(self.left.depth() if self.left else 0)
        
        if math.fabs(self.delta()) < 2:
            return
    
        if self.delta() < 0:
            # если разница отрицательная, значит левый
            if double_swap:
                self._swap_right_left()
            else:
                self._swap_left()
        else:
            # если разница положительная, значит правый
            if double_swap:
                self._swap_left_right()
            else:
                self._swap_right()

        

    def depth(self):
        """Возвращаем максимальную глубину ноды"""

        return max([self.left.depth() if self.left else 0, 
                    self.right.depth() if self.right else 0, self.level])

    def delta(self):
        """Разница уровней правой\левой веток"""

        return (self.left.depth() if self.left else 0) \
            - (self.right.depth() if self.right else 0)


    def removemin(self):
        """Возвращаем ноду без минимального элемента, возвращая его"""

        if not self.left:
            return self.right

        self.left = self.left.removemin()
        self.balance()
        return self

    def findmin(self):
        """
        Находим минимальный элемент в ноде. По свойству сбаллансированного дерева, 
        минимальный элемент в крайней левой ветке, если его нет — возвращаем его самого.
        """

        return self.left.findmin() if self.left else self

    def add(self, item):
        """ Добавляем элемент в ноду"""

        if not item:
            return

        if not isinstance(item, Node):
            item = Node(item, level=self.level+1)
        
        if item.level < self.level + 1:
            item.level += 1

        if self.value > item.value:
            # если новый эл-т больше, то шагаем в левую ветку
            if self.left:   
                self.left.add(item)
            else:
                self.left = item
        elif self.value < item.value:
            # иначе — в правую
            if self.right:   
                self.right.add(item)
            else:
                self.right = item

        # баллансируем
        self.balance()
        return item

class AVL(object):
    """
    Реализация структуры данных 'Сбаллансированное бинарное дерево'. Умеет искать\добавлять\удалять
    элементы, баллансировать себя
    """

    root = None

    def __init__(self, lst):
        """Инициализируем сбаллансированное бинарное дерево"""
        if len(lst) > 0:
            self.root = Node(lst[0])

            for i in lst[1:]:
                self.add(i)

    def __str__(self):
        return str(self.root._to_tree())
    
    def add(self, item):
        """Добавить элемент в дереве"""
        self.root.add(item)

    def remove(self, item, node=None):
        """Удалить элемент в дереве"""

        if not item:
            return 'Элемент не указан'

        if not node:
            # запускаем наш метод рекурсивно, переопределяя корень дерева
            self.root = self.remove(item, node=self.root)
            self.root.level = 0
            self.root.balance()
            return self.root
        
        if item < node.value:
            node.left = self.remove(item, node=node.left)
        elif item > node.value:
            node.right = self.remove(item, node=node.right)
        else:
            left, right = node.left, node.right
            del node
            
            if not right:
                return left

            min = right.findmin()
            min.right = right.removemin()
            min.left = left
            min.balance()
            return min
        
        node.balance()
        return node

    def find(self, value, node=None):
        """Найти элемент в дереве"""
        if not node:
            node = self.root
        
        if node.value is value:
            return node
        else:
            find_left = self.find(value, node=node.left) if node.left else False
            find_right = self.find(value, node=node.right) if node.right else False

            if find_left:
                return find_left
            elif find_right:
                return find_right
            
        return False

# Инициализируем дерево
awl_tree = AVL([7, 2, 6, 5, 8, 3, 1, 12, 10, 8])

# Ищем элемент три
print awl_tree.find(3)

# Выводим дерево в построенном виде
print awl_tree

# Удалаем элемент
awl_tree.remove(6)

# Выводим дерево с удаленным элементом
print awl_tree
