class Animal:
    legs = 4
    def __init__(self,name):
        self.name = name
    def speak(self):
        print('sound')

class Dog(Animal):
    pass

dog1 = Dog('lucky')
dog1.speak()

