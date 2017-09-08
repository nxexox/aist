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


    def _fix_levels(self):
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
        self.right._swap_right()
        self._swap_left()

    def _swap_left_right(self):
        self.left._swap_left()
        self._swap_right()

    def balance(self):
        """Балансировка дерева по ноде"""
    
        double_swap = math.fabs(self.right.depth() if self.right else 0) < math.fabs(self.left.depth() if self.left else 0)
        # print '%s, ld: %s, rd: %s' % (node.value, node.left.depth() if node.left else 0, node.right.depth() if node.right else 0)
        print 'node %s' % self.value
        print 'left depth %s' % (self.left.depth() if self.left else 0)
        print 'right depth %s' % (self.right.depth() if self.right else 0)
        print 'left node %s' % self.left
        print 'right node %s' % self.right
        print 'delta %s' % math.fabs(self.delta())
        print '----------'
        if math.fabs(self.delta()) < 2:
            return
    
        #print 'double swap %s' % double_swap
        if self.delta() < 0:
            if double_swap:
                print 'right_left'
                self._swap_right_left()
            else:
                print 'left'
                self._swap_left()
        else:
            if double_swap:
                print 'left_right'
                self._swap_left_right()
            else:
                print 'right'
                self._swap_right()

    def depth(self):
        return max([self.left.depth() if self.left else 0, 
                    self.right.depth() if self.right else 0, self.level])

    def delta(self):
        return (self.left.depth() if self.left else 0) - (self.right.depth() if self.right else 0)


    def removemin(self):
        if not self.left:
            return self.right

        self.left = self.left.removemin()
        self.balance()
        return self

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
        item = self.find(item)
        if not item:
            return 'Элемент не найден'

        min_node = item.findmin()

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
#awl_tree = AVL([7, 2, 6, 5, 8, 3,])
print awl_tree
print awl_tree.find(3)
print awl_tree.remove(3)
print awl_tree
#print awl_tree.find(1)
