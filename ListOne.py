from NodeF import NodeFloor

class simpleList():
    def __init__(self):
        self.firstt : NodeFloor = None
        self.lastt = None
        self.sizee = 0

    def lastInserted(self, nombre):
        newFloor = NodeFloor(nombre)
        self.sizee += 1
        if self.firstt is None:
            self.firstt = newFloor
            self.lastt = newFloor
        else:
            self.lastt.setNext(newFloor)
            self.lastt = newFloor
        return newFloor

    def promptInfo(self):
        temporary = self.firstt
        for i in range(self.sizee):
            #print(i, 'nombre:', temporary.getNombre(), 'row:', temporary.getRow(), 'column:', temporary.getColumn(), 'costosF:', temporary.getFcost(), 'costosS:', temporary.s)
            print(i,  'nombre:', temporary.nombre)
            temporary = temporary.getNext()
    





  