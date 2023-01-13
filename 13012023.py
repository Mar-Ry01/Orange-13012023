import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')
root = tree.getroot()

tytul = "Batman Returns"
print(tytul)
film_zmiana = root.find("./genre/decade/movie[@title='%s']/year" %tytul)
print("przed zmiana", film_zmiana.text)

film_zmiana.text = '2023'
print("po zmianie", film_zmiana.text)

