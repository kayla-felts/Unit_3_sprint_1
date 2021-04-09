import random


class Product:
    def __init__(self, name, price, weight, flammability=0.5,):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.identifier = random.randint(1000000, 9999999)
        self.flammability = float(flammability)

    def stealability(self):
        if (self.price / self.weight) < 0.5:
            return 'Not so stealable...'
        elif (self.price / self.weight) >= 0.5 < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very Stealable!!'

    def explode(self):
        if (self.flammability * self.weight) < 10:
            return '...fizzle.'
        elif (self.flammability * self.weight) >= 10 < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, price, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 5 < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
    
