import room
import mode
import corridor
import time
import maze_generator

class Dungeon:
    def __init__(self,floor, dungeon_type = 0):
        self.floor = floor
        self.width = self.floor.get_width()
        self.height = self.floor.get_height()
        self.type = dungeon_type
        # print("selftype is",self.type)
        self.layout = floor.get_floormap()
        self.current_mode = mode.layoutdict[self.type]
        self.rooms = {}
        self.corridors = []
        # print("selfmode is",self.current_mode)
        #time.sleep(1)

    def add_rooms(self,floordepth = 0):
        '''
        will split the dungeon in different sections, add one room in each section
        a room is a rectangle filled with '.' tile.
        it cannot exceed the size of the section, but can go as small as 1x1
        '''
        width = self.floor.get_width()
        height = self.floor.get_height()
        split_horizontal = self.current_mode['segments_x']
        split_vertical = self.current_mode['segments_y']
        horizontal_length = (width-3) / split_horizontal
        vertical_length = (height-3) / split_vertical
        # print("horizontal length is",horizontal_length)
        # print("vertical length is",vertical_length)
        for i in range(split_vertical):
            for j in range(split_horizontal):
                left_x = round(horizontal_length * j + 1)
                right_x = round(horizontal_length * (j+1) + 1)
                top_y = round(vertical_length * i + 1)
                bottom_y = round(vertical_length * (i+1) + 1)
                bounding_box = [left_x,right_x,top_y,bottom_y]
                # print('currently in new room function')
                # print("x min is:",left_x)
                # print("x max is:",right_x)
                # print("y min is:",top_y)
                # print("y max is:",bottom_y)
                new_room = room.Room(bounding_box,self.type,i,j)
                self.rooms[(i,j)] = new_room
                self.floor.add_new_room(bounding_box,new_room)
        pass

    def add_main_corridors(self):
        corridor_list = maze_generator.create_maze(self.current_mode['segments_y'],self.current_mode['segments_x'],self.current_mode['duplicated chance'])
        for corridor_connection in corridor_list:
            room1 = self.rooms[tuple(corridor_connection[0])]
            room2 = self.rooms[tuple(corridor_connection[1])]
            #print("room1 id",room1)
            #print("room2 id",room2)
            new_corridor = corridor.Corridor(room1,room2)
            self.corridors.append(new_corridor)
            self.floor.add_new_corridor(new_corridor)
        pass

    def __str__(self):
        return self.floor.return_map()
    
    def return_map(self):
        result = ''
        for i in self.layout:
            result += ''.join(i) + '\n'
        return result
    
