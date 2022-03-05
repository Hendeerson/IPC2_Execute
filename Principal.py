from lxml import etree as txt
import xml.etree.ElementTree as ET
from ListOne import *
from os import system
import os

listed = fillingInfo()


def searcher():
    searcherFile = filedialog.askopenfilename(title ='Getting xml Archive',initialdir = './', filetypes=(('xml files', '*.xml'),('all files','*.*')))
    xPath(searcherFile)



def xPath(ruta):
    #tree = ET.parse(ruta)
    #elementos = tree.xpath('//piso[@nombre="nombrePiso"]')
    #root = tree.getroot()

    # ET.dump(tree) #getting the xml information as it should be
    # print(root)
    #print(root)
    print('\n')

    content = open(ruta).read()
    floorArt = ET.fromstring(content)
    for floorArte in floorArt.iter("pisosArtesanales"):
        for floor in floorArte.iter("piso"):
            nombre = floor.attrib['nombre']
            #print(floor.tag)
            #print(floor.attrib['nombre'])
            #print(floor.text)
            R = ""
            C = ""
            F = ""
            S = ""
            patron = ""
            codigo = ""
            for row in floor.iter("R"):
                R += row.tag
                R += row.text  
                #print(row.tag, end=":" )
                #print(row.text)
            
            for column in floor.iter("C"):
                C += column.tag
                C += column.text  
                #print(column.tag, end=":" )
                #print(column.text)
               
            for fCost in floor.iter("F"):
                F += fCost.tag
                F += fCost.text 
                #print(fCost.tag, end=":" )
                #print(fCost.text)
               
            for sCost in floor.iter("S"):
                S += sCost.tag
                S += sCost.text  
                #print(sCost.tag, end=":" )
                #print(sCost.text)
            
            for pattern in floor.iter("patron"):
                codigo += pattern.attrib['codigo']
                #print(pattern.tag, end=": ")
                #print(pattern.attrib['codigo'])
                #print(pattern.text)
            listed.addingFloor(R, C, F, S, nombre)    
                #print(x)
            #print('')
                #listed.addingFloor(R, C, F, S, nombre)


xPath('P.xml')


#floorListt.promptInfo()


