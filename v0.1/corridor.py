import random

class Corridor:
    def __init__(self,room1,room2):
        self.room1 = room1
        self.room2 = room2
        self.corridor_list = []
        room1_cell_x = room1.get_x_coordinate()
        room2_cell_x = room2.get_x_coordinate()
        room1_cell_y = room1.get_y_coordinate()
        room2_cell_y = room2.get_y_coordinate()
        if room1_cell_x == room2_cell_x: #so this means they are horizontal
            if room1_cell_y < room2_cell_y:
                top_room =self.room1
                bottom_room = self.room2
            else:
                top_room = self.room2
                bottom_room = self.room1
            self.top_bottom_connection(top_room,bottom_room)
            pass
            
        else:
            if room1_cell_x < room2_cell_x:
                left_room = self.room1
                right_room = self.room2
            else:
                left_room = self.room2
                right_room = self.room1
            self.left_right_connection(left_room,right_room)
            pass

    def left_right_connection(self,left_room,right_room):
        left_room_door_x = left_room.get_x_max()+1
        left_room_door_y = random.randrange(left_room.get_y_min(),left_room.get_y_max()+1)
        self.corridor_list.append([left_room_door_y,left_room_door_x])
        right_room_door_x = right_room.get_x_min()-1
        right_room_door_y = random.randrange(right_room.get_y_min(),right_room.get_y_max()+1)
        self.corridor_list.append([right_room_door_y,right_room_door_x])

        turn_x_cord = random.randrange(left_room_door_x+1,right_room_door_x)
        for x in range(left_room_door_x+1,turn_x_cord):
            self.corridor_list.append([left_room_door_y,x])
        for x in range(turn_x_cord+1,right_room_door_x):
            self.corridor_list.append([right_room_door_y,x])
        for y in range(min(left_room_door_y,right_room_door_y),max(left_room_door_y,right_room_door_y)+1):
            self.corridor_list.append([y,turn_x_cord])
        pass

    def top_bottom_connection(self,top_room,bottom_room):
        top_room_door_y = top_room.get_y_max()+1
        top_room_door_x = random.randrange(top_room.get_x_min(),top_room.get_x_max()+1)
        self.corridor_list.append([top_room_door_y,top_room_door_x])
        bottom_room_door_y = bottom_room.get_y_min()-1
        bottom_room_door_x = random.randrange(bottom_room.get_x_min(),bottom_room.get_x_max()+1)
        self.corridor_list.append([bottom_room_door_y,bottom_room_door_x])

        turn_y_cord = random.randrange(top_room_door_y+1,bottom_room_door_y)
        for y in range(top_room_door_y+1,turn_y_cord):
            self.corridor_list.append([y,top_room_door_x])
        for y in range(turn_y_cord+1,bottom_room_door_y):
            self.corridor_list.append([y,bottom_room_door_x])
        for x in range(min(top_room_door_x,bottom_room_door_x),max(top_room_door_x,bottom_room_door_x)+1):
            self.corridor_list.append([turn_y_cord,x])
        pass
    
    def get_list(self):
        return self.corridor_list