# Instance attribute
class Dog:
    def __init__(self):
      # self is current instance
      # Assign value to self.attribute in __init__ method
      self.name = "Meron"
  
    def introduce(self):
      print("My name is " + self.name)

meron = Dog()
meron.introduce()


# Take values
class Person:
    def __init__(self, name, age, address):
        self.hello = "Hi"
        self.name = name
        self.age = age
        self.address = address
  
    def greeting(self):
        print('{0} I am {1}.'.format(self.hello, self.name))

mariko = Person('Mariko', 20, 'Nerima, Tokyo')
mariko.greeting()

print(mariko.name) # Instance attribute
print(mariko.age)
print(mariko.address)


# Add attribute after creating instance
class Cat:
   pass

kitty = Cat()
kitty.name = 'Kitty the cat'
print(kitty.name) # Kitty the cat

yonandmu = Cat()
print(yonandmu.name) # AttributeError: 'Cat' object has no attribute 'name'