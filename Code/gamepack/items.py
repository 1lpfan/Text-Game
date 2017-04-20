######
#Items
######

class Item():
    '''
    The base class for all items.
    '''
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
        
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
                         
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Bat(Weapon):
    def __init__(self):
        super().__init__(name="Baseball Bat",
                         description="A standard pre-war baseball bat.",
                         value=2,
                         damage=5)
 
 
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="An old, slightly rusted sword. More effective than a bat.",
                         value=10,
                         damage=20)

class Aid(Item):
    def __init__(self, name, description, value, bonus):
        self.bonus = bonus
        super().__init__(name, description, value)
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.bonus)

class FirstAidKit(Aid):
    def __init__(self):
        super().__init__(name='First Aid Kit',
                         description='A simple first aid kit to heal your wounds.',
                         value=15,
                         bonus=10)                             


                        