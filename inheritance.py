#child class inherits some/all features from the base/parent class
#Syntax: class derived-classname(superclass-name)

class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Pet):
    def __init__(self):