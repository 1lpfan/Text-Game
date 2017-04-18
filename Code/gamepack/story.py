######
#Story
######

import time

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
    global player
    player = raw_input('What is your name? >')
    print('Welcome, '+player)


def intro():
    '''
    Itroduces the player to the game with some of the background story
    '''
    print('The date is April 15, 2132')
    time.sleep(1)
    print('You entered the bunker exactly five years ago when the bombs began to fall.')
    print('The nuclear war decimated Earth, leaving only pockets of survivors.')
    time.sleep(5)
    print('Today is the day you will leave the safety of your bunker because your air scrubber is failing.')
    
def describe_bunker():
    '''
    Describes the starting room
    '''
    print('You wake up within the safe haven of your shelter, knowing you must leave and search for a new air scrubber.')
    time.sleep(3)
    print('You take a look around for any supplies you may need on your journey.')
    time.sleep(2)
    print('You take notice of a footlocker at the foot of your bed and the door leading out into the wasteland.')