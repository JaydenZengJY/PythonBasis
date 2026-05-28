import math

class Robot:
    def __init__(self, x, y, speed, direction, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.width = width
        self.height = height
        self.path = [(self.x, self.y)]
    
    def move(self):
        angle = math.radians(self.direction)

        dx = self.speed * math.cos(angle)
        dy = self.speed * math.sin(angle)

        self.x += dx
        self.y += dy

        self.check_collision()
        self.record_position()

    def check_collision(self):
        if self.x <= 0:
            self.x = 0
            self.direction = 180 - self.direction

        elif self.x >= self.width:
            self.x = self.width
            self.direction = 180 - self.direction

        if self.y <= 0:
            self.y = 0
            self.direction = -self.direction

        elif self.y >= self.height:
            self.y = self.height
            self.direction = -self.direction

        self.direction = self.direction % 360

    def record_position(self):
        self.path.append((self.x, self.y))

    def get_path(self):
        return self.path