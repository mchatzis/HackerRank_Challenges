import my_helper_functions as helpers

'''Find path to escape the maze (recursive backtracking)''' 

class MazeRunner():
    
    def __init__(self):
        self.location = (0,0) #Top-left of maze start
        self.destination = (4,4) #Top-right destination
        
    def __print_winning_path(self,path):
        print("winning path:")
        s = "" #string buffer
        
        for step in path:
            s += " -> " + str(step)
        print(s)
        
    def find_path(self,maze,path = [(0,0)]):
        x,y = self.location
        
        if maze[x][y] == 0:
            return False
        if self.location == self.destination:
            self.__print_winning_path(path)
            return True

        self.location = (self.location[0],self.location[1] + 1)
        path.append(self.location)
        if self.find_path(maze,path):
            return True
        else:
            self.location = (self.location[0],self.location[1] - 1) #backtrack
            path.pop(-1)
        
        self.location = (self.location[0] + 1, self.location[1])
        path.append(self.location)
        if self.find_path(maze,path):
            return True
        else:
            self.location = (self.location[0] - 1,self.location[1])
            path.pop(-1)
            
        return False


#1 stands for open path, 0 for closed path
Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]
        ]

#helpers.print_matrix(Maze)

runner = MazeRunner()
runner.find_path(Maze)