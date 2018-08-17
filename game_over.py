from kivy.uix.label import Label


class GameOver(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'GAME OVER\n' \
                    'Press Space to restart'
        self.font_size = 50
        self.color = 1, 1, 1, 0.5

    def on_texture_size(self, instance, value):
        if self.parent:
            while self.texture_size[0] > self.parent.width:
                self.font_size -= 1
                self.texture_update()



