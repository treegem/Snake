from kivy.core.window import Window
from kivy.properties import ObjectProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from snake import Snake


class SnakeGame(Widget):
    head = ObjectProperty(Snake)
    body = []

    def __init__(self):
        super().__init__()
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self
        )
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.history_pos = [(self.head.pos[0], self.head.pos[1])]
        self.history_v = [self.head.v]
        self.expand_snake = False

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        vx, vy = self.head.v
        if keycode[1] == 'up' and vy > -1:
            self.head.v = Vector(0, 1)
        elif keycode[1] == 'right' and vx > -1:
            self.head.v = Vector(1, 0)
        elif keycode[1] == 'down' and vy < 1:
            self.head.v = Vector(0, -1)
        elif keycode[1] == 'left' and vx < 1:
            self.head.v = Vector(-1, 0)
        elif keycode[1] == 'e':
            self.expand_snake = True

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def add_bodypart(self):
        self.add_dummy()
        new_bodypart = Snake(pos=self.history_pos[0])
        self.body.append(new_bodypart)
        self.add_widget(new_bodypart)
        self.expand_snake = False

    def add_dummy(self):
        dummy_bodypart = Snake(pos=(self.right - Snake.width.defaultvalue, self.y))
        self.add_widget(dummy_bodypart)

    def update_history_pos(self):
        self.history_pos[0] = (self.head.pos[0], self.head.pos[1])

    def update_history_v(self):
        self.history_v[0] = self.head.v

    def body_move(self):
        if len(self.body) > 0:
            self.body[0].v = self.history_v[0]
            self.body[0].move()

    def update(self, dt):
        self.update_history_pos()
        self.head.move()
        self.body_move()
        self.update_history_v()
        if self.expand_snake:
            self.add_bodypart()
