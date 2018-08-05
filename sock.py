from kivy.vector import Vector
from random import randint
from snake import Snake
from kivy.uix.widget import Widget


class Sock(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid_width, self.grid_height = 0, 0

    def on_parent(self, widget, parent):
        self.grid_width = int(self.parent.width / Snake.width.defaultvalue)
        self.grid_height = int(self.parent.height / Snake.height.defaultvalue)

    def spawn(self, ):
        self.pos = Vector(randint(0, self.grid_width), randint(0, self.grid_height))
