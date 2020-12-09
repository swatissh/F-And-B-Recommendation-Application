from Position import Position
import math
# get distance from students to CANTEEN
class Distance:
    def __init__(self):
        pass

    def getDistance(self,PositionX,PositionY):
        disX = math.pow(PositionX.x - PositionY.x, 2)
        disY = math.pow(PositionX.y - PositionY.y, 2)
        return math.sqrt(disX + disY)

if __name__ == "__main__":
    x = Position()
    x.setposition(1, 1)
    y = Position()
    y.setposition(2, 2)
    dis = Distance()
    print("distance is "+str(dis.getDistance(x,y)))