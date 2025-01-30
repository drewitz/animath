from manim import *

from modules.data_write import write_data

colourmain = "#5AD86A"
colourcomp = "#FF726B"
coloursec1 = "#5F7DC6"
coloursec2 = "#FFCE6B"

class Ableitung(Scene):
    """drawing an animation of the differential quotient"""
    meta_data = {
        "title": "Ableitung",
        "timestamps": [0],
        "filename": "Ableitung.mp4",
        "path": "videos/"
    }
    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))
    x0 = 0.5

    def p(self, x):
        return x**2+0.5

    def pprime(self, x):
        return 2*x

    def plot_secant(self, ax, h):
        slope = (self.p(self.x0 + h) - self.p(self.x0))/h
        return ax.plot(lambda x: self.p(self.x0) + (x-self.x0)*slope, color="green")

    def plot_line(self, ax):
        return ax.plot(lambda x: self.p(self.x0) + (x-self.x0)*self.pprime(self.x0), color="green")
    
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def new_x(self):
        x0 = self.xs[-1]
        return x0 - self.p(x0)/self.pprime(x0)

    def construct(self):
        self.draw_logo()
        ax = Axes(
            y_range=[-0.5, 5.5, 1],
            x_range=[-0.5, 2.5, 1]
        )

        graph = ax.plot(lambda x: self.p(x), x_range=[-2.5, 2.5], color="blue")
        self.play(Create(ax))
        self.play(Create(graph))
        self.add_timestamp()

        h = ValueTracker(1.5)
        dotx = Dot(color=colourmain).move_to(ax.c2p(self.x0+h.get_value(), self.p(self.x0+h.get_value())))
        dotx0 = Dot(color=colourcomp).move_to(ax.c2p(self.x0, self.p(self.x0)))
        dotx.add_updater(
            lambda x: x.move_to(ax.c2p(self.x0 + h.get_value(), self.p(self.x0+h.get_value())))
        )
        # labelx = DecimalNumber(
        #     self.x0 + h.get_value(), num_decimal_places=3, color=colourmain, show_ellipsis=True
        labelx0 = MathTex(
            "x_0", color=colourcomp
        ).next_to(ax.c2p(self.x0, 0), DOWN)
        labelx = MathTex(
            "x", color=colourmain
        )
        def label_updater(mobj):
            # mobj.set_value(self.x0 + h.get_value())
            mobj.next_to(ax.c2p(self.x0 + h.get_value(), 0), DOWN)

        labelx.add_updater(
            label_updater
        )
        secant = self.plot_secant(ax, h.get_value())
        secant.add_updater(
            lambda x: x.become(self.plot_secant(ax, h.get_value()))
        )
        self.play(Create(dotx), FadeIn(labelx))
        self.play(Create(dotx0), FadeIn(labelx0))
        self.play(FadeIn(secant))
        self.add_timestamp()
        self.play(h.animate.set_value(1))
        self.add_timestamp()
        self.play(h.animate.set_value(0.5))
        self.add_timestamp()
        self.play(h.animate.set_value(0.25))
        self.add_timestamp()
        self.play(h.animate.set_value(0.025))
        grenzwert = self.plot_line(ax)
        self.play(Transform(secant, grenzwert), FadeOut(dotx), FadeOut(labelx))

        self.add_timestamp()
        write_data(self.meta_data)
