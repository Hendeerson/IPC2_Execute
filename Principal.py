from lxml import etree as txt
import xml.etree.ElementTree as ET


def xPath(ruta):
    tree = ET.parse(ruta)
    #elementos = tree.xpath('//piso[@nombre="nombrePiso"]')
    root = tree.getroot()

    # ET.dump(tree) #getting the xml information as it should be
    #print(root)
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
    for elements in root:
        print(elements.tag, elements.text)
        print(elements.text)
        print(elements.attrib['nombre'])
        
        #patron = elements[0]
        for subelements in elements:
            print('*', subelements.tag, end= ":")
            print(subelements.text)
            #patrones = subelements[0]
            for p in subelements:
                print('-', p.tag, p.text)

    # for elements in root:
        # print(elements.tag)
        # print(elements.text)
        # for subelements in elements:
        # for sub2elemts in subelements:
        #print(sub2elemts.tag, end="")
        # print(sub2elemts.text)


'''
    for x in root.findall('.//'):
        
        print(x.tag, end=":")
        
        print(x.text, end="")
        print(x.attrib)'''


xPath('P.xml')
