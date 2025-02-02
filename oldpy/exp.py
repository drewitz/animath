from manim import *
from manim_slides import Slide
import numpy as np




common_kwargs = {"fill_opacity": 0.9}

class Teich(Slide):
    """drawing an animation of the Newton method"""
    step_num = 3
    width = 0.5
    height = 0.5/np.sqrt(2)
    pondw = 2**step_num*width
    pondh = 2**step_num*height

    def construct(self):
        day = Tex("Tag: ")
        daynum = Integer(0).next_to(day).align_to(day, UP)
        theday = VGroup(day, daynum).shift(self.pondh*DOWN)
        rose = Rectangle(width=self.width, height=self.height, color=GREEN, **common_kwargs).shift(
            (self.pondw - self.width)/2*LEFT + (self.pondh - self.height)/2*DOWN
        )
        pond = Rectangle(width=self.pondw, height=self.pondh, color=BLUE, **common_kwargs)
        self.play(FadeIn(pond), FadeIn(rose), FadeIn(theday))
        self.next_slide()

        for x in range(self.step_num):
            newrose = rose.copy()
            self.add(newrose)
            self.play(newrose.animate.shift(self.height*UP))
            daynum.set_value(2*x+1)
            self.height *= 2
            rose = VGroup(rose, newrose)
            self.next_slide()
            newrose = rose.copy()
            self.add(newrose)
            self.play(newrose.animate.shift(self.width*RIGHT))
            daynum.set_value(2*x+2)
            self.width *= 2
            rose = VGroup(rose, newrose)
            self.next_slide()


