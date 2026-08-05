
class Animal:

    def __init__(self,name):
        self.name = name 

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print("this animal is fleeing")
    pass

class Predator(Animal):
    def hunt(self):
        print("this animal is hunting")
    pass

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("meme")
hawk = Hawk("meuch")
fish = Fish("nemo")

rabbit.sleep()