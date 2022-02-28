class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.nextt= None

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name                   
    