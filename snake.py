from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class Snake(Widget):
    v = Vector(1, 0)
    width = NumericProperty(20)

    def move(self):
        self.pos = self.width * Vector(*self.v) + self.pos
