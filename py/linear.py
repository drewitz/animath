from manim import *
import json
import string

class Linear(Scene):
    """drawing an animation of the Newton method"""
    meta_data = {
        "title": "Reflections of Linear Functions",
        "timestamps": [0],
        "filename": "Linear.mp4",
        "path": "videos/"
    }
    a = 0.4
    b = -1.5
    ex_points = [-3, 1, 5] # x coordinates of example points.
    points = []
    labels = []

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

    def f(self, x):
        return self.a*x + self.b
    
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
            arrow = Arrow(stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow")
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))
        
        self.add_timestamp()
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
            arrow = Arrow(stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow")
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))
        
        self.add_timestamp()
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
            arrow = Arrow(stroke_width=2, max_tip_length_to_length_ratio=0.1, color="yellow")
            dest.append(arrow)
            arrow.put_start_and_end_on(self.points[i].get_center(), pt.get_center())
            self.play(FadeIn(lbl), FadeIn(arrow), FadeToColor(pt, RED))
        
        self.add_timestamp()
        graph = ax.plot(lambda x: -self.f(-x), color=RED)
        dest.append(graph)
        self.play(FadeIn(graph))

        return VGroup(*dest)

    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        ax = Axes(
            # y_range=[-3, 2.5, 1],
            # x_range=[-0.5, 2.5, 1]
        ).add_coordinates()
        ax_labels = ax.get_axis_labels()

        graph = ax.plot(lambda x: self.f(x), color="blue")
        self.play(Create(ax), FadeIn(ax_labels))
        #self.play(Create(ax_labels))
        self.play(Create(graph))
        self.add_timestamp()

        for i, x in enumerate(self.ex_points):
            pt = Dot(ax.coords_to_point(x, self.f(x)), color="green")
            lbl = MathTex(string.ascii_uppercase[i], color="green").next_to(pt)
            self.points.append(pt)
            self.labels.append(lbl)
            self.play(FadeIn(pt), Write(lbl))
        
        self.add_timestamp()
        
        for func in [self.reflect_y, self.reflect_x, self.reflect_origin]:
            refl = func(ax)
            self.add_timestamp()
            self.play(FadeOut(refl))
        self.add_timestamp()

        with open("data.json", "a") as f:
            f.write(json.dumps(self.meta_data, indent=2))
