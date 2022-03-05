from os import system
import os
# class for the informtion under R


class rowDoubList():
    def __init__(self):
        self.rowFirst = None
        self.rowLast = None

    def rowList(self, R):
        newRow = NodeFloorTemp(R)
        if self.rowFirst is None:
            self.rowFirst = newRow
            self.rowLast = self.rowFirst
        else:
            rl = self.rowLast
            rl.after = newRow
            self.rowFirst = rl.after
            self.rowLast.before = rl

    def rowFirstShow(self):
        rl = self.rowFirst
        while rl is not None:
            yield rl
            rl = rl.after
            print(rl)

    def rowLastShow(self):
        rl = self.rowLast
        while rl is not None:
            yield rl
            rl = rl.before
# class for the informtion under C


class columnDoubList():
    def __init__(self):
        self.columnFirst = None
        self.columnLast = None

    def columnList(self, C):
        newColumn = NodeFloorTemp(C)
        if self.columnFirst is None:
            self.columnFirst = newColumn
            self.columnLast = self.columnFirst
        else:
            cl = self.columnLast
            cl.after = newColumn
            self.columnFirst = cl.after
            self.columnLast.before = cl

    def columnFirstShow(self):
        cl = self.columnFirst
        while cl is not None:
            yield cl
            cl = cl.after

    def columnLastShow(self):
        cl = self.columnLast
        while cl is not None:
            yield cl
            cl = cl.before
# class for the informtion under F


class fCostDoubList():
    def __init__(self):
        self.fCostFirst = None
        self.fCostLast = None

    def fCostList(self, F):
        newFCost = NodeFloorTemp(F)
        if self.fCostFirst is None:
            self.fCostFirst = newFCost
            self.fCostLast = self.fCostFirst
        else:
            fc = self.fCostLast
            fc.after = newFCost
            self.fCostFirst = fc.after
            self.fCostLast.before = fc

    def fCostFirstShow(self):
        fc = self.fCostFirst
        while fc is not None:
            yield fc
            fc = fc.after

    def fCostLastShow(self):
        fc = self.fCostLast
        while fc is not None:
            yield fc
            fc = fc.before
# class for the informtion under S


class sCostDoubList():
    def __init__(self):
        self.sCostFirst = None
        self.sCostLast = None

    def sCostList(self, S):
        newSCost = NodeFloorTemp(S)
        if self.sCostFirst is None:
            self.sCostFirst = newSCost
            self.sCostLast = self.sCostFirst
        else:
            sc = self.sCostLast
            sc.after = newSCost
            self.sCostFirst = sc.after
            self.sCostLast.before = sc

    def sCostFirstShow(self):
        sc = self.sCostFirst
        while sc is not None:
            yield sc
            sc = sc.after

    def sCostLastShow(self):
        sc = self.sCostLast
        while sc is not None:
            yield sc
            sc = sc.before
# class for the informtion under Piso


class floorDoubList():
    def __init__(self):
        self.floorFirst = None
        self.floorLast = None

    def floorList(self, piso):
        newFloor = NodeFloorTemp(piso)
        if self.floorFirst is None:
            self.floorFirst = newFloor
            self.floorLast = self.floorFirst
        else:
            pl = self.floorLast
            pl.after = newFloor
            self.floorFirst = pl.after
            self.floorLast.before = pl

    def floorFirstShow(self):
        pl = self.floorFirst
        while pl is not None:
            yield pl
            pl = pl.after

    def floorLastShow(self):
        pl = self.floorLast
        while pl is not None:
            yield pl
            pl = pl.before
# R Node


class NodeR:
    def __init__(self, R):
        self.r1 = R
        self.c1 = columnDoubList()

    def setC(self, C):
        self.exist = False
        for col in self.c1.columnFirstShow():
            if col.data.c2 == C:
                self.exist = True
                return col
            if self.exist == False:
                return False

# C NODE


class NodeC:
    def __init__(self, C):
        self.c2 = C
        self.f1 = fCostDoubList()

    def setF(self, F):
        self.exist = False
        for fcost in self.f1.fCostFirstShow():
            if fcost.data.f3 == F:
                self.exist = True
                return fcost
            if self.exist == False:
                return False

 # F NODE


class NodeF:
    def __init__(self, F):
        self.f3 = F
        self.s1 = sCostDoubList()

    def setS(self, S):
        self.exist = False
        for scost in self.s1.sCostFirstShow():
            if scost.data.s2 == S:
                self.exist = True
                return scost
                print(scost)
            if self.exist == False:
                return False
# S NODE


class NodeS:
    def __init__(self, S):
        self.s2 = S
        self.piso2 = floorDoubList()

    def setFloor(self, piso):
        self.exist = False
        for piso3 in self.piso2.floorFirstShow():
            if piso3.data.floorName == piso:
                self.exist = True
                return piso3
            if self.exist == False:
                return False

 # FLOOR NODE


class NodeFloor:
    def __init__(self, nombre):
        self.floorName = nombre

    def __str__(self):
        return "Piso -> {}".format(self.floorName)


# TEMPORALITY
class NodeFloorTemp:
    def __init__(self, data):
        self.data = data
        self.after = None
        self.before = None


class fillingInfo:
    def __init__(self):
        self.rowList2 = rowDoubList()

    def addingFloor(self, R, C, F, S, nombre):
        R = ""
        C = ""
        F = ""
        S = ""
        nombre = ""
        data= []


        ro = R
        co = C
        fco = F
        sco = S

        name = nombre
        container = self.PisosArte(R)
        if container != False:
            R = container.data
            container = R.setC(co)
            if container != False:
                C = container.data
                container = C.setF(fco)
                if container != False:
                    F = container.data
                    container = F.setS(sco)
                    if container != False:
                        S = container.data
                        container = S.setFloor(nombre)
                        if container != False:
                            print("The information {} is already stored".format(
                                container.data.floorName))
                            
                        else:
                            newFloor = NodeFloor(name)
                            S.piso2.floorList(newFloor)
                    else:
                        newFloor = NodeFloor(name)
                        newSCost = NodeS(sco)
                        newSCost.piso2.floorList(newFloor)
                        F.s1.sCostList(newSCost)
                else:
                    newFloor = NodeFloor(name)
                    newSCost = NodeS(sco)
                    newSCost.piso2.floorList(newFloor)
                    newFCost = NodeF(fco)
                    newFCost.s1.sCostList(newSCost)
                    C.f1.fCostList(newFCost)
            else:
                newFloor = NodeFloor(name)
                newSCost = NodeS(sco)
                newSCost.piso2.floorList(newFloor)
                newFCost = NodeF(fco)
                newFCost.s1.sCostList(newSCost)
                newColumn = NodeC(co)
                newColumn.f1.fCostList(newFCost)
                R.c1.columnList(newColumn)
        else:
            newFloor = NodeFloor(name)
            newSCost = NodeS(sco)
            newSCost.piso2.floorList(newFloor)
            newFCost = NodeF(fco)
            newFCost.s1.sCostList(newSCost)
            newColumn = NodeC(co)
            newColumn.f1.fCostList(newFCost)
            newRow = NodeR(ro)
            newRow.c1.columnList(newColumn)
            self.rowList2.rowList(newRow)

    def PisosArte(self, dataa):
        self.exist = False
        for pisosArtesanales in self.rowList2.rowFirstShow():
            if pisosArtesanales.data.r1 == dataa:
                self.exist = True
                return pisosArtesanales
        if self.exist == False:
            return False
