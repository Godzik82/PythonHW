from abc import ABC, abstractmethod
from myexception import NoNodeClassError

class Node(ABC):

    def __init__(self, data):
        self.children = []
        self.data = data
        self.level = None

    def add_node(self, node):
        try:
            if not isinstance(node, Node):
                raise NoNodeClassError()
            else:
                node.children_append(node)
                self.children[-1].level = self.level + 1
                print(node.show_your_data())
        except NoNodeClassError:
            print('Неверный класс')

    @abstractmethod
    def children_append(self, node):
        self.children.append(node)

    @abstractmethod
    def show_your_data(self):
        return self.data

    @abstractmethod
    def show_yourself(self):
        return self

    
    def show_your_children(self):
        for child in self.children:
            print('Уровень дерева: ' + str(child.level) + ' NodeIndex: ' + str(self.children.index(child)), end=' ')
            print(child.show_your_data())
            if child.children != []:
                child.show_your_children()

class NodeText(Node):

    def show_your_data(self):
        return 'Здесь хранится текст: ' + super().show_your_data()

    def children_append(self, node):
        return super().children_append(node)

    def show_yourself(self):
        return super().show_yourself()   

class NodeNumber(Node):

    def show_your_data(self):
        return 'Здесь хранится число: ' + str(super().show_your_data())

    def children_append(self, node):
        return super().children_append(node)

    def show_yourself(self):
        return super().show_yourself()

class NotNode():
    data = 'Это не Node Class'

    def show_yourself(self):
        print('Ha Ha')

