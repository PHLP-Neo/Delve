import renderer
import time

class Floor:
    def __init__(self,dungeon_width = 52, dungeon_height = 28, dungeon_type = 0):
        self.width = dungeon_width
        self.height = dungeon_height
        self.floormap = []
        
        for i in range(dungeon_height):
            row = []
            for j in range(dungeon_width):
                if i == 0 or i == dungeon_height-1 or j == 0 or j == dungeon_width-1:
                    row.append('%')
                else:
                    row.append('#')
            self.floormap.append(row)

    def add_new_room(self,bounding_box, target_room):
        x_min = bounding_box[0]
        x_max = bounding_box[1]
        y_min = bounding_box[2]
        y_max = bounding_box[3]
        room_x_min = target_room.get_x_min()
        room_x_max = target_room.get_x_max()
        room_y_min = target_room.get_y_min()
        room_y_max = target_room.get_y_max()
        for i in range(y_min,y_max+1):
            for j in range(x_min,x_max+1):
                if i in range(room_y_min,room_y_max+1) and j in range(room_x_min,room_x_max+1):
                    self.floormap[i][j] = '.'
                    # print('Creating Rooms...')
                    # renderer.render_map(self)
                    # time.sleep(0.01)
                pass
        pass

    def add_new_corridor(self,corridorlist):
        for corridor_cood in corridorlist.get_list():
            x_cood = corridor_cood[1]
            y_cood = corridor_cood[0]
            self.floormap[y_cood][x_cood] = '+'
            # print('Creating Corridors...')
            # renderer.render_map(self)
            # time.sleep(0.01)

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_floormap(self):
        return self.floormap

    def return_map(self):
        result = ''
        for i in self.floormap:
            result += ''.join(i) + '\n'
        return result
    
    def __str__(self):
        result = ''
        for i in self.floormap:
            result += ''.join(i) + '\n'
        return result