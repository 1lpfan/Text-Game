###############################
#Bunker: A Text Based Adventure
###############################

import random
import time

def display_title():
    '''
    Displays Game title
    '''
    print('------------------------------------------')
    print('******Bunker: A Text Based Adventure******')
    print('------------------------------------------')

    # Wait 3 seconds
    time.sleep(3)
def player_name():
    '''
    Asks the player for their name and stores it as variable player 
    ''' 
    player = raw_input('What is your name? >')
    time.sleep(1)

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