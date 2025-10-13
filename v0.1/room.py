import random
import mode

class Room:
    room_dictionary = {}
    def __init__(self,bounding_box,dungeon_type,index_i,index_j):
        chance_for_empty_room = mode.layoutdict[dungeon_type][0]
        x_min = bounding_box[0]
        x_max = bounding_box[1]
        y_min = bounding_box[2]
        y_max = bounding_box[3]
        coordinate = [index_i,index_j]
        if random.random() < chance_for_empty_room:
            #just generate a single dot, aka fake room
            self.x_min = random.randint(x_min+2,x_max-2)
            self.x_max = self.x_min
            self.y_min = random.randint(y_min+2,y_max-2)
            self.y_max = self.y_min
        else:
            while True:
                x_value_1 = random.randint(x_min+2,x_max-2)
                x_value_2 = random.randint(x_min+2,x_max-2)
                if abs(x_value_2 - x_value_1) >= 3:
                    break
            while True:
                y_value_1 = random.randint(y_min+2,y_max-2)
                y_value_2 = random.randint(y_min+2,y_max-2)
                if abs(y_value_2 - y_value_1) >= 3:
                    break
            self.x_min = min(x_value_1,x_value_2)
            self.x_max = max(x_value_1,x_value_2)
            self.y_min = min(y_value_1,y_value_2)
            self.y_max = max(y_value_1,y_value_2)
        # print("called this function init function")
        # print("x min is:",self.x_min)
        # print("x max is:",self.x_max)
        # print("y min is:",self.y_min)
        # print("x max is:",self.y_max)
        pass

    def get_x_min(self):
        return self.x_min
    def get_y_min(self):
        return self.y_min

    def get_x_max(self):
        return self.x_max

    def get_y_max(self):
        return self.y_max
    
    def get_y_coordinate(self):
        return self.coordinate[0]
    
    def get_x_coordinate(self):
        return self.coordinate[1]