class values:
    def __init__(self, R, C, F, S):
        self.R = R #row
        self.C = C #column
        self.f = f #cost
        self.s = s
        self.nextV = None
        self.beforeV = None



    def getRow(self):
        return self.nextV

    def setRow(self, piso):
        self.nextV= piso

    def getRow(self):
        return self.beforeV

    def setRow(self, piso):
        self.beforeV= piso
    
    
