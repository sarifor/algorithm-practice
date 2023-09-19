# Class and method
class Person:
    def greeting(self): # Method must have self as first argument
        print("Konnichiwa")

# Use method
jerry = Person()
jerry.greeting() # Use method not via class, but instance


# Data types are classes as well
b = list(range(10))
b.append(11)
print(b) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(type(b)) # <class 'list'>
print(type(jerry)) # <class '__main__.Person'>


# Instance vs. object
a = list(range(11)) # a is list class' instance