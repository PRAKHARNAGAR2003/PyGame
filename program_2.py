
# Class, Object, and Method
class animal:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def run(self):
        print("Running...")
    def eat(self):
        print("Eating...")

dog = animal("paddle","White")
print(dog.breed)        

# Inheritance

class human:
    def speaking(self):
        print("Speaking...")

class german(human):
    pass

class french(human):
    pass

stephen = french()
stephen.speaking()