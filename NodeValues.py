class values:
    def __init__(self, R):#, C, F, S):
        self.R = R #row
        '''self.C = C #column
        self.f = f #cost
        self.s = s'''
        self.next = None
        self.before = None



    def getNext(self):
        return self.nextV

    def setNext(self, piso):
        self.next= piso

    def getBefore(self):
        return self.beforeV

    def setBefore(self, piso):
        self.before= piso
    
    
