import dungeon
import renderer
import entity
import player
import os

def play_cycle(new_dungeon,player1):
    while True:
        stop = player.player_movement(player1,new_dungeon.get_floor().get_floormap())
        #renderer.render_stacked(new_dungeon,player1)
        renderer.render_stacked_fog(new_dungeon,player1)
        if stop:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

if __name__ == "__main__":
    new_dungeon = dungeon.generate_dungeon(130,50,2)
    #renderer.render_stacked(new_dungeon.get_floor())
    player1_pos = new_dungeon.get_spawn_point()
    player1 = entity.Player(player1_pos[0],player1_pos[1])
    print("\033[H",end="")
    renderer.render_stacked_fog(new_dungeon,player1)
    play_cycle(new_dungeon,player1)