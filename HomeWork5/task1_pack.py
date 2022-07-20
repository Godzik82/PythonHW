from tree import Tree

def task1():
    t = Tree('Family')
    t.add_child('Father')
    t.add_child('Mother')
    t.add_child('Son')
    t.add_child('Dauther')
    t.get_all_childrens_names()