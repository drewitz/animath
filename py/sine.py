from manim import *
import numpy as np

from modules.data_write import write_data

# PARAMETERS
common_kwargs = {"fill_opacity": 0.5}

# COLOURS
colourmain = "#5AD86A"
colourcomp = "#FF726B"
coloursec1 = "#5F7DC6"
coloursec2 = "#FFCE6B"

class Sine(Scene):
    meta_data = {
        "title": "Sine",
        "timestamps": [0],
        "filename": "sine.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        # self.draw_logo()
        ax = Axes(x_range=[0, 6*PI], y_range=[-2, 2])

        phi = ValueTracker(2*PI)
        sine_line = ax.plot(lambda x: np.sin(x), x_range=[0, phi.get_value()]).add_updater(
            lambda x: x.become(ax.plot(lambda x: np.sin(x), x_range=[0, phi.get_value()]))
        )

        self.play(FadeIn(ax))
        self.play(Create(sine_line))
        self.wait(1)
        self.play(phi.animate.set_value(5*PI))
        self.play(phi.animate.set_value(3*PI))

        self.add_timestamp()
        write_data(self.meta_data)
