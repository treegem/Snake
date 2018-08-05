from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.vector import Vector

from snake import Snake


class SnakeGame(FloatLayout):
    head = ObjectProperty(Snake)
    body = []

    def __init__(self):
        super().__init__()

        self.history_pos = [(self.head.pos[0], self.head.pos[1])]
        self.history_v = [self.head.v]
        self.next_dir = self.head.v

        # Init keyboard
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self
        )
        self._keyboard.bind(on_key_down=self._on_key_down)

        self.expand_snake = False

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        vx, vy = self.head.v
        if keycode[1] == 'up' and vy > -1:
            self.next_dir = Vector(0, 1)
        elif keycode[1] == 'right' and vx > -1:
            self.next_dir = Vector(1, 0)
        elif keycode[1] == 'down' and vy < 1:
            self.next_dir = Vector(0, -1)
        elif keycode[1] == 'left' and vx < 1:
            self.next_dir = Vector(-1, 0)
        elif keycode[1] == 'e':
            self.food_snacked()

    def food_snacked(self):
        self.expand_snake = True

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def add_body_part(self):
        new_body_part = Snake(pos=self.history_pos[0])
        new_body_part.v = self.history_v[0]
        self.body.insert(0, new_body_part)
        self.add_widget(new_body_part)
        self.expand_snake = False
        self.history_pos.insert(0, ('dummy', 'dummy'))
        self.history_v.insert(0, self.head.v)

    def update_history_pos(self):
        for i, position in enumerate(self.history_pos[1:]):
            self.history_pos[i] = position
        self.history_pos[-1] = (self.head.pos[0], self.head.pos[1])

    def update_history_v(self):
        for i, v in enumerate(self.history_v[1:]):
            self.history_v[i] = v
        self.history_v[-1] = self.head.v

    def update_head_v(self):
        self.head.v = self.next_dir

    def body_move(self):
        if len(self.body) > 0:
            for i, snek in enumerate(self.body):
                snek.v = self.history_v[i+1]
                snek.move()

    def update(self, dt):
        self.update_history_pos()
        self.update_head_v()
        self.head.move()
        self.body_move()
        self.update_history_v()
        if self.expand_snake:
            self.add_body_part()
