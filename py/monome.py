from manim import *
import json

class Potenz(Scene):
    """drawing an animation of the Newton method"""
    meta_data = {
        "title": "Potenzfunktionen",
        "timestamps": [0],
        "filename": "Potenz.mp4",
        "path": "videos/"
    }
    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))
    
    n_max = 13

    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        ax = Axes(
        ).add_coordinates()
        ax_labels = ax.get_axis_labels()
        self.add(ax, ax_labels)
        text = MathTex("f(x) = \ldots").shift(4*RIGHT+2*UP)
        self.add(text)

        graph = None
        for n in range(self.n_max):
            newtext = MathTex(f"f(x) = x^{{{n}}}").shift(text.get_center())
            if graph is not None:
                new_graph = ax.plot(lambda x: x**n, x_range=[-2, 2], color="blue")

                self.play(Transform(graph, new_graph), Transform(text, newtext))
                # graph = new_graph
            else:
                graph = ax.plot(lambda x: x**n, color="blue")
                self.play(FadeIn(graph), Transform(text, newtext))
            self.add_timestamp()

        with open("data.json", "a") as f:
            f.write(json.dumps(self.meta_data, indent=2))
