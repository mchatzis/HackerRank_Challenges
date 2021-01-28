'''Case where robot ends on the axes is not covered. Comprehensive Testing is missing too'''
ORIGIN = (0,0)
LEFT = (-1,0)
RIGHT = (1,0)
UP = (0,1)
DOWN = (0,-1)

class Robot():
    
    def __init__(self):
        self.location = (0,0)
        self.direction = (0,1)
    
    def __turn(self,towards):
        if self.direction == LEFT:
            if towards == 'l':
                self.direction = DOWN
                return
            if towards == 'r':
                self.direction = UP
                return
        if self.direction == RIGHT:
            if towards == 'l':
                self.direction = UP
                return
            if towards == 'r':
                self.direction = DOWN
                return
        if self.direction == UP:
            if towards == 'l':
                self.direction = LEFT
                return
            if towards == 'r':
                self.direction = RIGHT
                return
        if self.direction == DOWN:
            if towards == 'l':
                self.direction = RIGHT
                return
            if towards == 'r':
                self.direction = LEFT
                return
        raise Exception("No if statement entered in turning function")

    def __extra_step_needed(self,tpl1,tpl2):
        '''At each quadrant, there exist two directions where robot has to perform
            an extra step before following the minimum path'''
        
        sign = lambda x: 1 if x > 0 else (0 if x == 0 else -1)
    
        if sign(tpl1[0]) == sign(tpl2[0]) or sign(tpl1[1] == sign(tpl2[1])):
            return True
        else:
            return False
        
    def move(self, walk):
        for step in walk:
            if step == 'f':
                self.location = (self.location[0]+self.direction[0],self.location[1]+self.direction[1])
            else:
                self.__turn(step)
    def print_loc(self):
        print(f"Robot is at: {self.location}")
        print(f"It's direction is: {self.direction}")
    
    def find_min_steps(self):
        x,y = self.location
        steps = abs(x) + abs(y)
        
        if self.__extra_step_needed(self.direction,self.location):
            steps += 2
        else:
            steps += 1
        return steps        

if __name__ == "__main__":
    
        robot_walk = ['l','f','f','r','f','f','f','f','f','f','f','f']
    
        robot = Robot()
        robot.move(robot_walk)
        robot.print_loc()
        print(robot.find_min_steps())
