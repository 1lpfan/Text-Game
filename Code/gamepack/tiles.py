######
#Tiles
######

import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()
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
        The exit door is straight ahead and your closet is to the right.
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
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
      
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
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
 
class GiantSpiderRoom(EnemyRoom):
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
        super().__init__(x, y, items.Sword())
 
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

