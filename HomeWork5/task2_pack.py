from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def task2():
    dot = Digraph('Family', 'Family graph')

    dot.node('A', 'Семья')
    dot.node('B', 'Папа')
    dot.node('C', 'Мама')
    dot.node('D', 'Сын')
    dot.node('E', 'Дочь')

    dot.edges(['AB', 'AC', 'AD', 'AE'])

    dot.render('HomeWork5/test.gv', view=True)