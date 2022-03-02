from lxml import etree as txt
import xml.etree.ElementTree as ET
from ListOne import simpleList

floorListt = simpleList()


def xPath(ruta):
    tree = ET.parse(ruta)
    #elementos = tree.xpath('//piso[@nombre="nombrePiso"]')
    root = tree.getroot()

    # ET.dump(tree) #getting the xml information as it should be
    # print(root)
    print(root)
    print('\n')

    '''
    #print('Etiquetas colores')
    for e in root:
        print('etiquetas', e.tag)
        print('valor', e.text)
        print(e.attrib, '\n')
        print('Atributes')
    for elements in root.findall('.//'):
        print(elements.attrib)

        print(elements.tag)
        print(elements.text)'''

# print('\n')
# print('Values')
    '''
    #verdadero
    for elements in root:
        print(elements.tag, end =": ")
        print(elements.attrib['nombre'])
        print(elements.text)
        
        
        #patron = elements[0]
        for subelements in elements:
            print('*', subelements.tag, end= ":")
            print(subelements.text)
            #patrones = subelements[0]
            for p in subelements:
                print('-', p.tag, end = ': ')
                print(p.text)
        print('\n')
        '''

    '''
    for x in root.findall('.//'):
        
        print(x.tag, end=":")
        
        print(x.text, end="")
        print(x.attrib)'''

    for reviewR in root:
        nombre = reviewR.text.replace('\n', '')
        floorListt.lastInserted(reviewR.attrib['nombre'])
        R= reviewR[0]
        print(nombre)
        for rr in R:
            #print('_',  rr.tag)
            #floorListt.lastInsertedV(rr .attrib['R'])
           print(rr.text)
        


xPath('P.xml')
floorListt.promptInfo()

