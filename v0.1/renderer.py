import copy

memory_map = []

def render_map(floor):
    floor_map = floor.return_map()
    for i in floor.__str__():
        #return
        match i:
            case "%":
                print("\x1b[38;5;245m█\x1b[0m",end="")
            case '#':
                print("\x1b[38;5;130m▓\x1b[0m",end="")
            case '.':
                print("\x1b[38;5;40m░\x1b[0m",end="")
            case '+':
                print("\x1b[38;5;226m▓\x1b[0m",end="")
            case _:
                print(i,end="")
    print("\033[H",end="")

def render_stacked(dungeon,player):
    stacked_render = copy.deepcopy(dungeon.get_floor().get_floormap())
    #initialize player memory map
    global memory_map
    if memory_map == []:
        memory_map = copy.deepcopy(dungeon.get_floor().get_floormap())
        for i in range(len(memory_map)):
            for j in range(len(memory_map[0])):
                memory_map[i][j] = " "

    player_pos = player.get_coordinate()
    update_memory_map(player_pos[0],player_pos[1],dungeon)

    stacked_render[player_pos[0]][player_pos[1]] = 'p'
    #old render method
    for row in stacked_render:
        for element in row:
        #return
            match element:
                case "%":
                    print("\x1b[38;5;245mE\x1b[0m",end="")
                case '#':
                    print("\x1b[38;5;130mW\x1b[0m",end="")
                case '.':
                    print("\x1b[38;5;40mR\x1b[0m",end="")
                case '+':
                    print("\x1b[38;5;226mC\x1b[0m",end="")
                case 'p':
                    print("☺",end="")
                case _:
                    print(element,end="")
        print("\n",end="")
    print("\033[H",end="")

def render_stacked_fog(dungeon,player):
    #stacked_render = copy.deepcopy(dungeon.get_floor().get_floormap())
    #initialize player memory map
    global memory_map
    if memory_map == []:
        memory_map = copy.deepcopy(dungeon.get_floor().get_floormap())
        for i in range(len(memory_map)):
            for j in range(len(memory_map[0])):
                memory_map[i][j] = " "

    player_pos = player.get_coordinate()
    y = player_pos[0]
    x = player_pos[1]
    update_memory_map(y,x,dungeon)

    
    #old render method
    dungeon_map = dungeon.get_floor().get_floormap()
    if dungeon_map[y][x] == '.':
        for room in dungeon.rooms.values():
            if y <= room.get_y_max() and y >= room.get_y_min() and x <= room.get_x_max() and x >= room.get_x_min():
                target_room = room
                break
        # now we found the room   
        for i in range(target_room.get_y_min()-1,target_room.get_y_max()+2):
            for j in range(target_room.get_x_min()-1,target_room.get_x_max()+2):
                memory_map[i][j] = dungeon_map[i][j]
        pass
        y_min = target_room.get_y_min()-1
        y_max = target_room.get_y_max()+1
        x_min = target_room.get_x_min()-1
        x_max = target_room.get_x_max()+1
    # this means in corridor
    elif dungeon_map[y][x] == '+':
        y_min = y-1
        y_max = y+1
        x_min = x-1
        x_max = x+1

    memory_map[y][x] = 'p'

    for i in range(len(memory_map)):
        for j in range(len(memory_map[0])):
            if i <= y_max and i >= y_min and j <= x_max and j >= x_min:
                element = memory_map[i][j]
                match element:
                    case "%":
                        print("\x1b[38;5;245m▓\x1b[0m",end="")
                    case '#':
                        print("\x1b[38;5;130m▓\x1b[0m",end="")
                    case '.':
                        print("\x1b[38;5;40m░\x1b[0m",end="")
                    case '+':
                        print("\x1b[38;5;226m░\x1b[0m",end="")
                    case 'p':
                        print("☺",end="")
                    case _:
                        print(element,end="")
            else:
                element = memory_map[i][j]
                match element:
                    case "%":
                        print("\x1b[38;5;237m▓\x1b[0m",end="")
                    case '#':
                        print("\x1b[38;5;237m▓\x1b[0m",end="")
                    case '.':
                        print("\x1b[38;5;249m░\x1b[0m",end="")
                    case '+':
                        print("\x1b[38;5;249m░\x1b[0m",end="")
                    case 'p':
                        print("☺",end="")
                    case _:
                        print(element,end="")
        print("\n",end="")
    print("\033[H",end="")

def update_memory_map(y,x,dungeon):
    dungeon_map = dungeon.get_floor().get_floormap()
    global memory_map
    # this means in room
    if dungeon_map[y][x] == '.':
        for room in dungeon.rooms.values():
            if y <= room.get_y_max() and y >= room.get_y_min() and x <= room.get_x_max() and x >= room.get_x_min():
                target_room = room
                break
        # now we found the room   
        for i in range(target_room.get_y_min()-1,target_room.get_y_max()+2):
            for j in range(target_room.get_x_min()-1,target_room.get_x_max()+2):
                memory_map[i][j] = dungeon_map[i][j]
        pass
    # this means in corridor
    elif dungeon_map[y][x] == '+':
        for i in range(y-1,y+2):
            for j in range(x-1,x+2):
                memory_map[i][j] = dungeon_map[i][j]
        pass