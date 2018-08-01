from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class Snake(Widget):
    vx = NumericProperty(0)
    vy = NumericProperty(0)
    v = ReferenceListProperty(vx, vy)
    v = Vector(1, 0)

    def move(self):
        self.pos = self.width * Vector(*self.v) + self.pos
