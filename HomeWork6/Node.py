from abc import ABC, abstractmethod

class Node(ABC):

    def __init__(self, data):
        self.children = []
        self.data = data
        self.level = None

    def add_node(self, data):
        if isinstance(data, str):
            self.children.append(NodeText(data))
        elif isinstance (data, (float, int)):
            self.children.append(NodeNumber(data))
        else:
            print('Неправильно указан параметр')
        self.children[-1].level = self.level + 1

    @abstractmethod
    def show_your_data(self):
        return self.data

    
    def show_your_children(self):
        for child in self.children:
            print('Уровень дерева: ' + str(child.level) + ' NodeIndex: ' + str(self.children.index(child)), end=' ')
            print(child.show_your_data())
            if child.children != []:
                child.show_your_children()

class NodeText(Node):

    def show_your_data(self):
        return 'Здесь хранится текст: ' + super().show_your_data()

class NodeNumber(Node):

    def show_your_data(self):
        return 'Здесь хранится число: ' + str(super().show_your_data())

