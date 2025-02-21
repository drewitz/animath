from manim import *
from manim_slides import Slide


class DistanzEbenePunkt(Slide):
    def construct(self):
        width = 4
        height = 2
        plane = Polygon(
            [width + height / 2, height, 0],
            [height / 2 - width, height, 0],
            [-height / 2 - width, -height, 0],
            [-height / 2 + width, -height, 0],
            fill_color=BLUE,
            fill_opacity=0.5,
        ).shift(DOWN)
        px = 2.5
        py = 4
        punktp = Dot([px, py, 0]).shift(DOWN)
        punkts = Dot([px, height / 3, 0]).shift(DOWN)
        gerade = Line([px, py, 0], [px, height / 3, 0]).shift(DOWN)
        self.play(Create(plane))
        self.next_slide()
        self.play(FadeIn(punktp))
        self.next_slide()
        self.play(FadeIn(punkts), FadeIn(gerade))
