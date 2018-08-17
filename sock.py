from kivy.vector import Vector
from random import randint
from snake import Snake
from kivy.uix.widget import Widget


class Sock(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid_width, self.grid_height = 0, 0

    def update_grid_width(self, value):
        self.grid_width = int(value / Snake.width.defaultvalue)

    def update_grid_height(self, value):
        self.grid_height = int(value / Snake.height.defaultvalue)

    def spawn(self, forbidden_positions=[]):
        self.pos = Vector(randint(0, max(1, self.grid_width - 1)) * Snake.width.defaultvalue,
                          randint(0, max(1, self.grid_height - 1)) * Snake.height.defaultvalue)
