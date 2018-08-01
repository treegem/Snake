from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from snake import Snake


class SnakeGame(Widget):
    snake = ObjectProperty(Snake)

    def update(self, dt):
        self.snake.move()
