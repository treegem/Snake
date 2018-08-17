from kivy.uix.label import Label


class GameOver(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'GAME OVER\n' \
                    'Press Space to restart'
        self.font_size = 50
        self.color = 1, 1, 1, 0.5



