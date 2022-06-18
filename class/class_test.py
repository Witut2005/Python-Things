
class Person:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell_somenthing(self):
        print('My name is', self.name, '. My age is', self.age)



tomek = Person(input(), input())

tomek.tell_somenthing()


