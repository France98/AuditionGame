class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0


class Arrow(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arrow = Arrow(self, 200, 200)
        

    def update(self, delta):
        self.update(delta)