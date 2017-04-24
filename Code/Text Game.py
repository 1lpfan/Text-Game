###############################
#Bunker: A Text Based Adventure
###############################

import gamepack.world as world
from gamepack.player import Player as Player

def play():
    world.load_tiles()
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = str(raw_input('Action: '))
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break