from NodeValues import values

class ListDT():
    def __init__(self):
        self.firstt = None
        self.lastt= None
        self.sizee = 0

    def lastInsertedV(self, R):
        newValues = values(R)
        self.sizee += 1
        if self.firstt is None:
            self.firstt = newValues
            self.lastt = newValues
        else:
            self.lastt.setNext(newValues)
            newValues.setBefore(self.lastt)
            self.lastt = newValues  

    def promptInfoV(self):
        temporary = self.firstt
        while temporary is not None:
            #print(temporary.R)
            #print('R:', temporary.R, 'row:', temporary.getRow(), 'column:', temporary.getColumn(), 'costosF:', temporary.getFcost(), 'costosS:', temporary.s)
            print('R:', temporary.R)
            temporary = temporary.getNext()