from myexception import NoNodeClassError
from tree import Tree
from Node import NodeNumber, NodeText, NotNode

def task2():
    tree = Tree('Дерево')
    a = NodeNumber(1)
    b = NodeText('1')
    c = NotNode()
    print(type(c))
    # print(tree.node)
    # tree.create_node(a)
    try:
        tree.create_node(c)
    except NoNodeClassError:
        print('Неверный класс')
    # tree.create_node(c)
    tree.create_node(b)
    
    tree.node.add_node(b)
    tree.node.add_node(a)
    tree.node.add_node(c)
    tree.node.add_node(b)

# task2()
    