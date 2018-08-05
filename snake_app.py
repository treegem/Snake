from kivy.app import App
from kivy.clock import Clock

from snake_game import SnakeGame


class SnakeApp(App):
    title = 'Sweet Georgie Brown\'s Snek Game'

    def build(self):
        game = SnakeGame()
        Clock.schedule_interval(game.update, 1.0 / 10.0)
        return game
