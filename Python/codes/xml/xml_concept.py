import xml.sax
import pathlib


class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("---Person---")
            print("Id: {}".format(attrs["id"]))

    # Chunk of characters i.e value of element or attribute
    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print("->Name: {}".format(self.name))
        elif self.current == "age":
            print("->Age: {}".format(self.age))
        elif self.current == "weight":
            print("->Weight: {}".format(self.weight))
        elif self.current == "height":
            print("->Height: {}".format(self.height))
        self.current = ""  # require this other wise height will printed twice


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
# parser.parse(pathlib.Path.cwd() / "Python/codes/xml" / "persons.xml")
parser.parse("Python/codes/xml/persons.xml")  # relative path to project `concepts`
