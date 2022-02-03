from manim import *
import json

class Newton(Scene):
    """drawing an animation of the Newton method"""
    meta_data = {
        "title": "Animation of the Newton method",
        "timestamps": [0],
        "filename": "Newton.mp4",
        "path": "videos/"
    }
    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))
    x0 = 0.5
    xs = [x0]
    lines = []
    step_num = 3

    def p(self, x):
        return x**2 - 2

    def pprime(self, x):
        return 2*x

    def plot_line(self, ax):
        x0 = self.xs[-1]
        return ax.plot(lambda x: self.p(x0) + (x-x0)*self.pprime(x0), color="green")
    
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def new_x(self):
        x0 = self.xs[-1]
        return x0 - self.p(x0)/self.pprime(x0)

    def construct(self):
        self.draw_logo()
        ax = Axes(
            y_range=[-3, 2.5, 1],
            x_range=[-0.5, 2.5, 1]
        ).add_coordinates()
        ax_labels = ax.get_axis_labels()

        graph = ax.plot(lambda x: self.p(x), x_range=[-2.5, 2.5], color="blue")
        self.play(Create(ax), FadeIn(ax_labels))
        #self.play(Create(ax_labels))
        self.play(Create(graph))
        self.add_timestamp()

        x0 = self.xs[0]
        
        for step in range(self.step_num):
            vert_line = ax.plot_line_graph([x0, x0], [0, self.p(x0)], add_vertex_dots=False)
            self.play(Create(vert_line))
            new_line = self.plot_line(ax)
            self.play(Create(new_line))
            self.add_timestamp()
        
            x0 = self.new_x()
            self.xs.append(x0)
        
        with open("data.json", "a") as f:
            f.write(json.dumps(self.meta_data, indent=2))
