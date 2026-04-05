import math

class Segment:
    def __init__(self, name=None):
        self.name = name

    def to_dict(self):
        return self.__dict__

class Straight(Segment):
    def __init__(self, length, name=None):
        super().__init__(name)
        self.type = "straight"
        self.length = length


class Corner(Segment):
    def __init__(self, radius, angle, name=None):
        super().__init__(name)
        self.type = "corner"
        self.radius = radius
        self.angle = angle 

    def arc_length(self):
        return math.radians(self.angle) * self.radius
    