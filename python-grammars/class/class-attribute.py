# Class attribute
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff) # Not show bag is class attribute, as self is current instance

josuke = Person()
josuke.put_bag('Book')

joruno = Person()
joruno.put_bag('Key')

print(josuke.bag) # ['Book', 'Key']
print(joruno.bag) # ['Book', 'Key']


# Class attribute accessed by class name
class Person:
    bag = []
    
    def put_bag(self, stuff):
        Person.bag.append(stuff) # Shows bag is clsss attribute