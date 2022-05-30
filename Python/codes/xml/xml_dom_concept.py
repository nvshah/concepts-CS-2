import xml.dom.minidom

domtree = xml.dom.minidom.parse("Python/codes/xml/persons.xml")
group = domtree.documentElement

persons = group.getElementsByTagName("person")

# Read --------------------
for p in persons:
    print("---Person---")
    if p.hasAttribute("id"):
        print("ID: {}".format(p.getAttribute("id")))

    print("Name: {}".format(p.getElementsByTagName("name")[0].childNodes[0].data))
    print("Age: {}".format(p.getElementsByTagName("age")[0].childNodes[0].data))
    print("Weight: {}".format(p.getElementsByTagName("weight")[0].childNodes[0].data))
    print("Height: {}".format(p.getElementsByTagName("height")[0].childNodes[0].data))


"""
Remember -> Node means any of {element, attribute, value(element val or attribute val)}

"""
# MAnipulation --------------
persons[-1].getElementsByTagName("name")[0].childNodes[0].nodeValue = "Manohar"
persons[0].setAttribute("id", "100")
# Changes made above are only on python object so lets reflect them in file(i.e persons.xml)
domtree.writexml(open("Python/codes/xml/persons.xml", "w"))


# Add New Node --------------

p = domtree.createElement("person")
p.setAttribute("id", "3")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Priya"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("23"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("90"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("180"))

p.appendChild(name)
p.appendChild(age)
p.appendChild(weight)
p.appendChild(height)

domtree.writexml(open("Python/codes/xml/persons.xml", "w"))
