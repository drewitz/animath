from manim import *
import numpy as np

from modules.data_write import write_data


class SquareCompletion(Scene):
    """completion of the square"""
    meta_data = {
        "title": "Quadratische Ergänzung",
        "timestamps": [],
        "filename": "SquareCompletion.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()

        a, x2, p1, b, x, p2, c, eq, zero = MathTex(
            "a", "x^2", "+", "b", "x", "+", "c", "=", "0"
        )
        part1 = VGroup(a, x2, p1, b, x)
        equation1 = VGroup(part1, p2, c, eq, zero)
        self.play(FadeIn(equation1, lag_ratio=0.2, run_time=2))
        self.add_timestamp()

        part1a = MathTex("a", "x^2", "+", "a", "\\frac{b}{a}", "x").next_to(p2, LEFT)
        self.play(
            Transform(part1, part1a),
            run_time=2
        )
        self.add_timestamp()
        part1b = MathTex("a", "\\left(x^2", "+", "\\frac{b}{a}", "x\\right)").next_to(p2, LEFT)
        self.play(
            Transform(part1[3], part1b[0]),
            Transform(part1[:3], part1b[1:3]),
            Transform(part1[4:], part1b[3:]),
            run_time=2
        )
        self.add_timestamp()

        self.wait(2)

        # write_data(self.meta_data)