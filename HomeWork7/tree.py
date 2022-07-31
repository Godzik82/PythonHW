from Node import NodeNumber, NodeText, Node
from myexception import NoNodeClassError

class Tree:
    
    def __init__(self, name):
        self.name = name
        self.node = None

    def create_node(self, node):
        if self.node != None:
            print('Место для Node уже занято')
        elif not isinstance(node, Node):
            raise NoNodeClassError()
        else:
            self.node = node
            self.node.level = 1
            print(node.show_your_data())

        # elif node.isclass():
        #     print('Это не класс')
            
        
        # else:
        #     try:
        #         self.node = node.show_yourself()
        #         self.node.level = 1  
        #     except Exception as ex:
        #         print(ex)
        #         print('В дереве создается класс, который не унаследован от Node: ')
        

    def get_name(self):
        print(self.name)

    def walk(self):
        if self.node != None:
            print('Уровень дерева: ' + str(self.node.level) + ' ' + self.node.show_your_data())
            self.node.show_your_children()
        else:
            print('Здесь пусто')
