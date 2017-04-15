######
#Story
######


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