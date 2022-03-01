from BoxesListed import BoxesList
from PatternListed import patternList

class NodeFloor:
    def __init__(self, nombre, r, c, f, s):
        self.nombre = nombre
        self.r = r #row
        self.c = c #column
        self.f = f #cost
        self.s = s
        self.next = None
        self.pattern = PatternListed()
        self.box = BoxesListed()
        
    def beginBox(self):
        self.structureListC.newNode()
        


    def getPiso(self):
        return self.piso

    def setPiso(self, piso):
        self.piso = piso
    
    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next()

    