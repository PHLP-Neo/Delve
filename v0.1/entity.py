import floor

class Entity:
    def __init__(self,y_axis,x_axis):
        self.x = x_axis
        self.y = y_axis

    def get_coordinate(self):
        return [self.y,self.x]
    
    def move_up(self,floormap):
        if floormap[self.y-1][self.x] != '#':
            self.y -= 1

    def move_down(self,floormap):
        if floormap[self.y+1][self.x] != '#':
            self.y += 1

    def move_left(self,floormap):
        if floormap[self.y][self.x-1] != '#':
            self.x -= 1

    def move_right(self,floormap):
        if floormap[self.y][self.x+1] != '#':
            self.x += 1

class Player(Entity):
    pass