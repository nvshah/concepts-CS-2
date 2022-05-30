from collections import namedtuple

Person = namedtuple('Person', 'firstname lastname')


class Persons:
    def __init__(self, shinobies):
        self._shinobies = [s.firstname.upper() + ' ' + s.lastname.title() for s in shinobies]

    def __iter__(self):
        #Delegating the iterator protocol instead of implementing it
        return iter(self._shinobies)

ninjas = [
    Person('naruto', 'uzumaki'),
    Person('Sasuke', 'Uchiha'),
    Person('Sakura', 'Uchiha')
]

persons = Persons(ninjas)

for p in persons:
    print(p)