######
#Tiles
######

import items, enemies, actions, world, random
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        pass
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves
class StartingRoom(MapTile):
    def intro_text(self):
        return '''
        You wake up within the safe haven of your shelter,
        knowing you must leave and search for a new air scrubber.
        You take a look around for any supplies you may need on your journey.
        The exit door is straight ahead to the north and your closet is to the east.
        '''
 
    def modify_player(self, player):
        #Room has no action on player
        pass
     
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            self.damage = random.randint(1, self.enemy.damage)
            the_player.hp -= self.damage
            if the_player.hp > 0:  
                print("Enemy does {} damage. You have {} HP remaining.".format(self.damage, the_player.hp))
            else:
                print('You have died!')
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()
      
class LootRoom(MapTile):
    def __init__(self, x, y, item, item2):
        self.item = item
        self.item2 = item2
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
        player.inventory.append(self.item2)
 
    def modify_player(self, player):
        self.add_loot(player)

class Desert(MapTile):
    def intro_text(self):
        return """
        A desert wasteland
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class SpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Spider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant irradiated spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class Closet(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Bat(), items.FirstAidKit())
    def intro_text(self):
        return '''
        Rummaging through your closet proves quite useful, as you find a baseball
        bat and a first aid kit.
        '''

class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword(), None)
 
    def intro_text(self):
        return """
        You find a sword burried under the desert sand and pick it up.
        """

class ExitRoom(MapTile):
    def intro_text(self):
        return '''
        You open the sealed lead door and emerge from your bunker in a brutal
        desert wasteland.
        '''
        def modify_player(self, player):
            pass
class CaveRoom(MapTile):
    def intro_text(self):
        return '''
        You enter the cave and see something shiny sitting on a rock.
        You have found the Air Scrubber! You return to the safety of your bunker
        to breathe clean air once again.
        '''
    def modify_player(self, player):
        player.victory = True

class IguanaRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Iguana())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant irradiated Iguana blocks your path.
            """
        else:
            return """
            The corpse of a dead iguana lays lifeless on the ground.
            """

class CrabRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crab())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant angry irradiated crab guards the enterance to a cave
            to the west.
            """
        else:
            return """
            The lifeless body of a large crab lays on the ground.
            """




