from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
roc1 = Rocket(10,34)
roc1.x
roc1.y
roc1.print_rocket()
roc1.move_rocket(12, 44)
roc1.print_rocket()