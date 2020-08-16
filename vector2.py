
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        combinedX = self.x + other.x
        combinedY = self.y + other.y
        return Vector2(combinedX, combinedY)
    
    @staticmethod
    def getAllDirections():
        return [Vector2(0, -1), Vector2(1, -1), Vector2(1, 0), Vector2(1, 1), Vector2(0, 1), Vector2(-1, 1), Vector2(-1, 0), Vector2(-1, -1)]