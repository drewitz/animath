from manim import *
from manim_slides import Slide
import string


class Linear(Slide):
    """drawing an animation of the Newton method"""

    a = 0.4
    b = -1.5
    ex_points = [-3, 1, 5]  # x coordinates of example points.
    points = []
    labels = []

    def f(self, x):
        return self.a * x + self.b

    def reflect_y(self, ax):
        # reflect along y-axis
        dest = []
        for i, x in enumerate(self.ex_points):
            pt = self.points[i].copy()
            dest.append(pt)
            self.add(pt)
            self.play(pt.animate.move_to(ax.coords_to_point(-x, self.f(x))))
            lbl = MathTex(string.ascii_uppercase[i] + "'", color="red").next_to(pt)
            dest.append(lbl)
            arrow = Arrow(
                stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow"
            )
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))

        self.next_slide()
        graph = ax.plot(lambda x: self.f(-x), color=RED)
        dest.append(graph)
        self.play(FadeIn(graph))
        return VGroup(*dest)

    def reflect_x(self, ax):
        # reflect along x-axis
        dest = []
        for i, x in enumerate(self.ex_points):
            pt = self.points[i].copy()
            dest.append(pt)
            self.add(pt)
            self.play(pt.animate.move_to(ax.coords_to_point(x, -self.f(x))))
            lbl = MathTex(string.ascii_uppercase[i] + "'", color="red").next_to(pt)
            dest.append(lbl)
            arrow = Arrow(
                stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow"
            )
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))

        self.next_slide()
        graph = ax.plot(lambda x: -self.f(x), color=RED)
        dest.append(graph)
        self.play(FadeIn(graph))

        return VGroup(*dest)

    def reflect_origin(self, ax):
        # reflect at origin
        dest = []
        for i, x in enumerate(self.ex_points):
            pt = self.points[i].copy()
            dest.append(pt)
            self.add(pt)
            self.play(pt.animate.move_to(ax.coords_to_point(-x, -self.f(x))))
            lbl = MathTex(string.ascii_uppercase[i] + "'", color="red").next_to(pt)
            dest.append(lbl)
            arrow = Arrow(
                stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow"
            )
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))

        self.next_slide()
        graph = ax.plot(lambda x: -self.f(-x), color=RED)
        dest.append(graph)
        self.play(FadeIn(graph))

        return VGroup(*dest)

    def construct(self):
        ax = Axes(
            # y_range=[-3, 2.5, 1],
            # x_range=[-0.5, 2.5, 1]
        ).add_coordinates()
        ax_labels = ax.get_axis_labels()

        graph = ax.plot(lambda x: self.f(x), color="blue")
        self.play(Create(ax), FadeIn(ax_labels))
        # self.play(Create(ax_labels))
        self.play(Create(graph))
        self.next_slide()

        for i, x in enumerate(self.ex_points):
            pt = Dot(ax.coords_to_point(x, self.f(x)), color="green")
            lbl = MathTex(string.ascii_uppercase[i], color="green").next_to(pt)
            self.points.append(pt)
            self.labels.append(lbl)
            self.play(FadeIn(pt), Write(lbl))

        self.next_slide()

        for func in [self.reflect_y, self.reflect_x, self.reflect_origin]:
            refl = func(ax)
            self.next_slide()
            self.play(FadeOut(refl))
