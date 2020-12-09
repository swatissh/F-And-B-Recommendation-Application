# position of students and CANTEEN
class Position:
    def __init__(self , x = 0, y = 0):
        self.x = x
        self.y = y
    def setposition(self, x, y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getxy(self):
        return self.x,self.y

if __name__ == "__main__":
    pass