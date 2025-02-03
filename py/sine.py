from manim import *
from manim_slides import Slide
import numpy as np



# PARAMETERS
common_kwargs = {"fill_opacity": 0.5}

# COLOURS
colourmain = "#5AD86A"
colourcomp = "#FF726B"
coloursec1 = "#5F7DC6"
coloursec2 = "#FFCE6B"

class Sine(Slide):
    def construct(self):
        axmax = 1.7
        n = 8 # multiples of 90*DEGREES to plot
        ax1 = Axes(
            x_range=[-axmax, axmax], y_range=[-axmax, axmax], x_length=2*axmax, y_length=2*axmax
            )
        ax2 = Axes(
            x_range=[0, n*90*DEGREES, 90*DEGREES], y_range=[-axmax, axmax], x_length=8, y_length=2*axmax
            ).add_coordinates({i*90*DEGREES: MathTex(90*i) for i in range(1, n)})
        ax2.move_to([2, 0, 0])
        phi_label = ax2.get_x_axis_label(MathTex("\\varphi"), direction=DOWN, buff=0.4)
        ax1.next_to(ax2, LEFT)

        phi = ValueTracker(0)
        # left part
        # origin to point on circle
        op = Line(
            ax1.coords_to_point(0, 0),
            ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value()))
        ).add_updater(
            lambda x: x.become(
                Line(
                    ax1.coords_to_point(0, 0),
                    ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value()))
                )
            )
        )
        angle = Arc(radius=0.2, angle=phi.get_value(), arc_center=ax1.coords_to_point(0, 0)).add_updater(
            lambda x: x.become(Arc(radius=0.2, angle=phi.get_value(), arc_center=ax1.coords_to_point(0, 0)))
            )
        unicirc = Circle(1, color=coloursec1).move_to(ax1.coords_to_point(0, 0))
        unipoint = Dot(ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())), color=colourcomp)
        unipoint.add_updater(
            lambda x: x.move_to(ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())))
        )
        pA = ax1.coords_to_point(0, 0)
        triangle = Polygon(
            pA,
            ax1.coords_to_point(np.cos(phi.get_value()), 0),
            ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())),
            color=coloursec2
        )
        triangle.add_updater(
            lambda x: x.become(Polygon(
                pA,
                ax1.coords_to_point(np.cos(phi.get_value()), 0),
                ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())),
                color=coloursec2
            ))
        )

        # right part
        sine_line = ax2.plot(lambda x: np.sin(x), x_range=[0, phi.get_value()], color=colourmain)
        sine_line.add_updater(
            lambda x: x.become(ax2.plot(lambda x: np.sin(x), x_range=[0, phi.get_value()], color=colourmain))
        )

        point = Dot(ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value())), color=colourcomp)
        point.add_updater(
            lambda x: x.become(
                Dot(ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value())), color=colourcomp)
            )
        )
        vline = Line(
            ax2.coords_to_point(phi.get_value(), 0),
            ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value()))
        ).add_updater(
            lambda x: x.become(
                Line(
                    ax2.coords_to_point(phi.get_value(), 0),
                    ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value()))
                )
            )
        )
        # connection
        hline = DashedLine(
            ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())),
            ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value()))
        ).add_updater(
            lambda x: x.become(
                DashedLine(
                    ax1.coords_to_point(np.cos(phi.get_value()), np.sin(phi.get_value())),
                    ax2.coords_to_point(phi.get_value(), np.sin(phi.get_value()))
                )
            )
        )

        # screenplay
        self.add(ax1, ax2)
        self.add(triangle)
        self.add(unicirc, angle)
        self.add(hline, vline, sine_line, point, unipoint, phi_label)
        self.wait(1)
        self.play(phi.animate.set_value(80*DEGREES))
        self.play(phi.animate.set_value(30*DEGREES))
        self.play(phi.animate.set_value(70*DEGREES))
        self.play(phi.animate.set_value(15*DEGREES))
        self.next_slide()
        self.play(phi.animate.set_value(150*DEGREES), FadeOut(triangle), FadeIn(op), run_time=3)
        self.play(phi.animate.set_value(500*DEGREES), run_time=6)

