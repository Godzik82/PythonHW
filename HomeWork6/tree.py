from Node import NodeNumber, NodeText

class Tree:
    
    def __init__(self, name):
        self.name = name
        self.node = None

    def create_node(self, data):
        if self.node != None:
            print('Место для Node уже занято')
        elif isinstance(data, str):
            print('Создан объект NodeText')
            self.node = NodeText(data)
        elif isinstance (data, (float, int)):
            print('Создан объект NodeNumber')
            self.node = NodeNumber(data)
        else:
            print('Неправильно указан параметр') 
        self.node.level = 1       

    def get_name(self):
        print(self.name)

    def walk(self):
        if self.node != None:
            print('Уровень дерева: ' + str(self.node.level) + ' ' + self.node.show_your_data())
            self.node.show_your_children()
        else:
            print('Здесь пусто')
