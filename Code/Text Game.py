###############################
#Bunker: A Text Based Adventure
###############################

import random
import time

import gamepack.story as story

player_hp = 100
    
def attack(weapon_damage, enemy_hp):
    '''
    Defines the parameters of attacking.
    weapon_damage is the max hp damage the weapon can deal.
    enemy_hp is the hp value of the enemy.
    '''
    damage = random.randint(1,weapon_damage)
    enemy_hp = enemy_hp - damage
    time.sleep(.5)
    if enemy_hp <= 0:
        print('Enemy defeated!')
    else:
        print('Enemy Hit Points: '+ str(enemy_hp)) 
                
def enemy_attack(enemy_damage, player_hp):
    '''
    Defines the parameters of an enemy attacking the player.
    enemy damage is the max hp damage the enemy can deal.
    player_hp is the player's hp value.
    '''
    player_damage = random.randint(1, enemy_damage)
    player_hp = player_hp - player_damage
    time.sleep(.5)
    if player_hp <= 0:
        print('You have died!')
    else:
        print('Your Hit Points: ' + str(player_hp))
        



