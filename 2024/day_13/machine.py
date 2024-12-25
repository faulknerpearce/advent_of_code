class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"X {self.x} Y {self.y}"

class Button:
    def __init__(self, x, y, cost):
        self.movement = Coord(x, y)
        self.cost = cost
    
    def __repr__(self):
        return f"{self.movement} Cost {self.cost}"
  
class MachineConfig:
    def __init__(self, ax, ay, bx, by, prize_x, prize_y):
        self.a = Button(ax, ay, 3)
        self.b = Button(bx, by, 1)
        self.prize = Coord(prize_x, prize_y)

    def __repr__(self):
        return f"Button. A: {self.a}. B: {self.b}."
