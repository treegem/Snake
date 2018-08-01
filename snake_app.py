from kivy.app import App
from kivy.clock import Clock

from snake_game import SnakeGame


class SnakeApp(App):

    def build(self):
        game = SnakeGame()
        Clock.schedule_interval(game.update, 1.0 / 3.0)
        return game
