from manim import *
from manim_slides import Slide
import numpy as np


class SquareCompletion(Slide):
    """completion of the square"""

    def construct(self):
        a, x2, p1, b, x, p2, c, eq, zero = MathTex(
            "a", "x^2", "+", "b", "x", "+", "c", "=", "0"
        )
        part1 = VGroup(a, x2, p1, b, x)
        equation1 = VGroup(part1, p2, c, eq, zero)
        self.play(FadeIn(equation1, lag_ratio=0.2, run_time=2))
        self.next_slide()

        part1a = MathTex("a", "x^2", "+", "a", "\\frac{b}{a}", "x").next_to(p2, LEFT)
        self.play(Transform(part1, part1a), run_time=2)
        self.next_slide()
        part1b = MathTex("a", "\\left(x^2", "+", "\\frac{b}{a}", "x\\right)").next_to(
            p2, LEFT
        )
        self.play(
            Transform(part1[3], part1b[0]),
            Transform(part1[:3], part1b[1:3]),
            Transform(part1[4:], part1b[3:]),
            run_time=2,
        )
