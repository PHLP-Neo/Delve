import dungeon

def render_map(dungeon):
    dungeon_map = dungeon.return_map()
    for i in dungeon.__str__():
        #return
        match i:
            case "%":
                print("\x1b[38;5;245m█\x1b[0m",end="")
            case '#':
                print("\x1b[38;5;130m▓\x1b[0m",end="")
            case '.':
                print("\x1b[38;5;40m░\x1b[0m",end="")
            case _:
                print(i,end="")
    print("\033[H",end="")