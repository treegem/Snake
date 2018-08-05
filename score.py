from kivy.uix.label import Label


class Score(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
