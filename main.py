from snake_app import SnakeApp
from kivy.config import Config

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
Config.write()

if __name__ == '__main__':
    app = SnakeApp()
    app.run()
