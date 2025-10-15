import keyboard

def player_movement(player,floormap):
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'w' or event.name == 'up':
            player.move_up(floormap)
            #print("Action for 'w'")
            pass
        elif event.name == 'a' or event.name == 'left':
            player.move_left(floormap)
            #print("Action for 'd'")
            pass
        elif event.name == 's' or event.name == 'down':
            player.move_down(floormap)
            #print("Action for 'd'")
            pass
        elif event.name == 'd' or event.name == 'right':
            player.move_right(floormap)
            #print("Action for 'd'")
        elif event.name == 'esc':
            #print("Action for 'd'")
            return 1
    return 0