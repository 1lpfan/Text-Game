###############################
#Bunker: A Text Based Adventure
###############################

import random
import time

player_hp = 100

def display_title():
    '''
    Displays Game title
    '''
    print('------------------------------------------')
    print('******Bunker: A Text Based Adventure******')
    print('------------------------------------------')

def player_name():
    '''
    Asks the player for their name and stores it as variable player 
    ''' 
    player = raw_input('What is your name? >')
    print('Welcome, '+player)


def intro():
    '''
    Itroduces the player to the game with some of the background story
    '''
    print('The date is April 2nd, 2132')
    time.sleep(1)
    print('You entered the bunker exactly five years ago when the bombs began to fall.')
    print('The nuclear war decimated Earth, leaving only pockets of survivors.')
    time.sleep(5)
    print('Today is the day you will leave the safety of your bunker because your supplies are dangerously low.')
    
def attack(weapon_damage, enemy_hp):
    '''
    Defines the parameters of basic combat.
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
        



