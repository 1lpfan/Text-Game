########
#Enemies
########

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0
        
class Spider(Enemy):
    def __init__(self):
        super().__init__(name='Irradiated Spider', hp=10, damage=3)
 
 
class Crab(Enemy):
    def __init__(self):
        super().__init__(name='Irradiated Crab', hp=30, damage=20)
        
class Iguana(Enemy):
    def __init__(self):
        super().__init__(name= 'Irradiated Iguana', hp=15, damage=5)
