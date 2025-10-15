import dungeon
import renderer
import os
import time
import floor

def generate_dungeon(dungeon_width = 60, dungeon_height = 34, dungeon_type = 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    new_floor = floor.Floor(dungeon_width,dungeon_height)
    new_dungeon = dungeon.Dungeon(new_floor,dungeon_type)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Creating Walls...")
    renderer.render_map(new_floor)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    new_dungeon.add_rooms()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Room Created')
    renderer.render_map(new_floor)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    new_dungeon.add_main_corridors()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Corridor Created')
    renderer.render_map(new_floor)
    time.sleep(2)

if __name__ == "__main__":
    generate_dungeon(100,30,1)