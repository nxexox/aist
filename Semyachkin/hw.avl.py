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
        return 'Node(value: {}, level: {}, l:{}, r:{})\n'.format(self.value, self.level, 
            self.left.value if self.left else '', self.right.value if self.right else '')

    def _to_tree(self):
        return '{root:_>{level}}\n{left:_>{level}}{right:_>{level}}'.format(
            root = self.value, level = self.level * 4,
            left = self.left._to_tree() if self.left else '{:_>{}}\n'.format('#l', self.level * 4 + 4),
            right = self.right._to_tree() if self.right else '{:_>{}}\n'.format('#r', self.level * 4 + 4))

    def depth(self):
        return max([self.left.depth() if self.left else 0, 
                    self.right.depth() if self.right else 0, self.level])

    def delta(self):
        return self.left.depth() if self.left else 0 - self.right.depth() if self.right else 0

    def add(self, item):
        if not item:
            return

        if not isinstance(item, Node):
            item = Node(item, level=self.level+1)
        
        if item.level < self.level + 1:
            item.level += 1

        if self.value > item.value:
            if self.left:   
                self.left.add(item)
            else:
                self.left = item
        elif self.value < item.value:
            if self.right:   
                self.right.add(item)
            else:
                self.right = item

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

    def _fix_levels(self, node):
        if node.left:
            if node.left.level is not node.level + 1:
                node.left.level = node.level + 1
            node.left = self._fix_levels(node.left)
        if node.right:
            if node.right.level is not node.level + 1:
                node.right.level = node.level + 1
            node.right = self._fix_levels(node.right)
        
        return node

    def _swap_left(self, node):
        if not node.right:
            return node
        node = Node(node.right.value, 
                    right=node.right.right if node.right.right else None, 
                    left=Node(
                        node.value, 
                        right=node.right.left if node.right and node.right.left else None, 
                        left=node.left if node.left else None, 
                        level=node.level+1), 
                    level=node.level)

        return self._fix_levels(node)

    def _swap_right(self, node):
        if not node.left:
            return node
        node = Node(node.left.value, 
                    left=node.left.left if node.left.left else None, 
                    right=Node(
                        node.value, 
                        right=node.right if node.right else None, 
                        left=node.left.right if node.left and node.left.right else None, 
                        level=node.level+1), 
                    level=node.level)
                    
        return self._fix_levels(node)

    def _swap_right_left(self, node):
        node.right = self._swap_right(node.right)
        return self._swap_left(node)

    def _swap_left_right(self, node):
        node.left = self._swap_left(node.left)
        return self._swap_right(node)

    def _balance(self, node=None):
        """Балансировка дерева по ноде"""
        if not node:
            node = self.root
            
        double_swap = node.right.depth() if node.right else 0 >= node.left.depth() if node.left else 0
        print '%s, ld: %s, rd: %s' % (node.value, node.left.depth() if node.left else 0, node.right.depth() if node.right else 0)

        if math.fabs(node.delta()) < 2:
            return node
        else:
            if node.delta() < 0:
                if not double_swap:
                    node = self._swap_right_left(node)
                else:
                    node = self._swap_left(node)
            else:
                if not double_swap:
                    node = self._swap_left_right(node)
                else:
                    node = self._swap_right(node)
            return node

    def add(self, item):
        """Добавить элемент в дереве"""
        self.root.add(item)
        self.root = self._balance()

    def remove(self, item):
        """Удалить элемент в дереве"""
        pass

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

awl_tree = AVL([7, 2, 6, 5, 8, 3, 1, 12, ])
# awl_tree = AVL([7, 2, 6, ])
print awl_tree
#print awl_tree.find(1)
