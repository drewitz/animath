from manim import *
from manim_slides import Slide


colourmain = "#5AD86A"
colourcomp = "#FF726B"
coloursec1 = "#5F7DC6"
coloursec2 = "#FFCE6B"


class AbleitungMitH(Slide):
    """drawing an animation of the differential quotient"""

    x0 = 0.5

    def p(self, x):
        return x**2 + 0.5

    def pprime(self, x):
        return 2 * x

    def plot_secant(self, ax, h):
        slope = (self.p(self.x0 + h) - self.p(self.x0)) / h
        return ax.plot(lambda x: self.p(self.x0) + (x - self.x0) * slope, color="green")

    def plot_line(self, ax):
        return ax.plot(
            lambda x: self.p(self.x0) + (x - self.x0) * self.pprime(self.x0),
            color="green",
        )

    def new_x(self):
        x0 = self.xs[-1]
        return x0 - self.p(x0) / self.pprime(x0)

    def construct(self):
        ax = Axes(y_range=[-0.5, 5.5, 1], x_range=[-0.5, 2.5, 1])

        graph = ax.plot(lambda x: self.p(x), x_range=[-2.5, 2.5], color="blue")
        self.play(Create(ax))
        self.play(Create(graph))

        h = ValueTracker(1.5)
        dotx_axis = Dot(color=colourmain).move_to(
            ax.c2p(self.x0 + h.get_value(), 0)
        )
        dotx0_axis = Dot(color=colourcomp).move_to(
            ax.c2p(self.x0, 0)
        )
        dotx = Dot(color=colourmain).move_to(
            ax.c2p(self.x0 + h.get_value(), self.p(self.x0 + h.get_value()))
        )
        dotx0 = Dot(color=colourcomp).move_to(ax.c2p(self.x0, self.p(self.x0)))
        dotx.add_updater(
            lambda x: x.move_to(
                ax.c2p(self.x0 + h.get_value(), self.p(self.x0 + h.get_value()))
            )
        )
        dotx_axis.add_updater(
            lambda x: x.move_to(
                ax.c2p(self.x0 + h.get_value(), 0)
            )
        )
        # labelx = DecimalNumber(
        #     self.x0 + h.get_value(), num_decimal_places=3, color=colourmain, show_ellipsis=True
        labelx0 = MathTex("x", color=colourcomp).next_to(ax.c2p(self.x0, 0), DOWN+LEFT)
        labelx = MathTex("x+h", color=colourmain)
        #braceh = BraceBetweenPoints(ax.c2p(self.x0, 0), ax.c2p(self.x0+h.get_value()))

        #def brace_updater(mobj):
        #    mobj.set(point_2=ax.c2p(self.x0+h.get_value()))
        #braceh.add_updater(brace_updater)

        def label_updater(mobj):
            # mobj.set_value(self.x0 + h.get_value())
            mobj.next_to(ax.c2p(self.x0 + h.get_value(), 0), DOWN+RIGHT)

        labelx.add_updater(label_updater)
        secant = self.plot_secant(ax, h.get_value())
        secant.add_updater(lambda x: x.become(self.plot_secant(ax, h.get_value())))

        slopedx = Line(
            ax.c2p(self.x0, self.p(self.x0)),
            ax.c2p(self.x0+h.get_value(), self.p(self.x0)),
            color=coloursec2
        )
        slopedy = Line(
            ax.c2p(self.x0+h.get_value(), self.p(self.x0)),
            ax.c2p(self.x0+h.get_value(), self.p(self.x0 + h.get_value())),
            color=coloursec1
        )
        labeldx = MathTex("h", color=coloursec2).next_to(slopedx, DOWN)
        labeldy1 = MathTex("f(x + h)", color=coloursec1).next_to(slopedy, RIGHT)
        labeldy2 = MathTex(" - f(x)", color=coloursec1).next_to(labeldy1, DOWN)
        labeldy = VGroup(labeldy1, labeldy2)

        self.play(Create(dotx0), Write(labelx0), Create(dotx0_axis))
        self.next_slide()
        self.play(Create(dotx), Write(labelx), Create(dotx_axis))
        self.play(Create(secant))
        self.next_slide()
        self.play(Create(slopedx), Create(slopedy), Write(labeldx), Write(labeldy))
        self.next_slide()
        self.play(Uncreate(slopedx), Uncreate(slopedy), Unwrite(labeldx), Unwrite(labeldy))
        #self.play(h.animate.set_value(1))
        #self.next_slide()
        #self.play(h.animate.set_value(0.5))
        #self.next_slide()
        #self.play(h.animate.set_value(0.25))
        #self.next_slide()
        self.play(h.animate.set_value(0.025), run_time=5)
        grenzwert = self.plot_line(ax)
        self.play(Transform(secant, grenzwert), FadeOut(dotx), FadeOut(labelx), FadeOut(dotx_axis))

class Ableitung(Slide):
    """drawing an animation of the differential quotient"""

    x0 = 0.5

    def p(self, x):
        return x**2 + 0.5

    def pprime(self, x):
        return 2 * x

    def plot_secant(self, ax, h):
        slope = (self.p(self.x0 + h) - self.p(self.x0)) / h
        return ax.plot(lambda x: self.p(self.x0) + (x - self.x0) * slope, color="green")

    def plot_line(self, ax):
        return ax.plot(
            lambda x: self.p(self.x0) + (x - self.x0) * self.pprime(self.x0),
            color="green",
        )

    def new_x(self):
        x0 = self.xs[-1]
        return x0 - self.p(x0) / self.pprime(x0)

    def construct(self):
        ax = Axes(y_range=[-0.5, 5.5, 1], x_range=[-0.5, 2.5, 1])

        graph = ax.plot(lambda x: self.p(x), x_range=[-2.5, 2.5], color="blue")
        self.play(Create(ax))
        self.play(Create(graph))
        self.next_slide()

        h = ValueTracker(1.5)
        dotx = Dot(color=colourmain).move_to(
            ax.c2p(self.x0 + h.get_value(), self.p(self.x0 + h.get_value()))
        )
        dotx0 = Dot(color=colourcomp).move_to(ax.c2p(self.x0, self.p(self.x0)))
        dotx.add_updater(
            lambda x: x.move_to(
                ax.c2p(self.x0 + h.get_value(), self.p(self.x0 + h.get_value()))
            )
        )
        # labelx = DecimalNumber(
        #     self.x0 + h.get_value(), num_decimal_places=3, color=colourmain, show_ellipsis=True
        labelx0 = MathTex("x_0", color=colourcomp).next_to(ax.c2p(self.x0, 0), DOWN)
        labelx = MathTex("x", color=colourmain)

        def label_updater(mobj):
            # mobj.set_value(self.x0 + h.get_value())
            mobj.next_to(ax.c2p(self.x0 + h.get_value(), 0), DOWN)

        labelx.add_updater(label_updater)
        secant = self.plot_secant(ax, h.get_value())
        secant.add_updater(lambda x: x.become(self.plot_secant(ax, h.get_value())))
        self.play(Create(dotx), FadeIn(labelx))
        self.play(Create(dotx0), FadeIn(labelx0))
        self.play(FadeIn(secant))
        self.next_slide()
        self.play(h.animate.set_value(1))
        self.next_slide()
        self.play(h.animate.set_value(0.5))
        self.next_slide()
        self.play(h.animate.set_value(0.25))
        self.next_slide()
        self.play(h.animate.set_value(0.025))
        grenzwert = self.plot_line(ax)
        self.play(Transform(secant, grenzwert), FadeOut(dotx), FadeOut(labelx))
