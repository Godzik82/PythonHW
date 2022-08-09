class Snake():

    
    def __init__(self):
        self.body = [[10, 10]]

    def move(self, x, y):
        self.body.insert(0, [x, y])

    def eat(self):
        self.body.append(self.body[-1])
