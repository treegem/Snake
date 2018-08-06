from kivy.uix.label import Label


class Score(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0

    def reset(self):
        self.text = "0"
        self.score = 0
