from kivy.core.window import Window
from kivy.properties import ObjectProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from snake import Snake


class SnakeGame(Widget):
    head = ObjectProperty(Snake)
    body = ObjectProperty(Snake(pos=(10, 10)))

    def __init__(self):
        super().__init__()
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self
        )
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.add_widget(self.body)
        self.add_widget(Snake(pos=(600, self.y)))

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

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def update(self, dt):
        pass

