from kivy.config import Config

from snake_app import SnakeApp

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

if __name__ == '__main__':
    app = SnakeApp()
    app.run()
