class Tree:
    
    childrens = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def add_child(self, name):
        self.childrens.append(Tree(name))

    def get_all_childrens_names(self):
        child_names = []
        for child in self.childrens:
            child_names.append(child.name)
        print('''Family's members: ''', end='')
        print(*child_names, sep=', ', end='.')