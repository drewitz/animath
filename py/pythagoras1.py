from manim import *
from manim_slides import Slide
import numpy as np


# PARAMETERS
a = 2.5
b = 4
c = np.sqrt(a**2 + b**2)
common_kwargs = {"fill_opacity": 0.5}

# COLOURS
colourmain = "#5AD86A"
colourcomp = "#FF726B"
coloursec1 = "#5F7DC6"
coloursec2 = "#FFCE6B"


class Pythagoras1(Slide):
    def construct(self):
        # Create first triangle and move it down
        triangle = Polygon(
            [0, 0, 0], [b, 0, 0], [0, a, 0], color=colourmain, **common_kwargs
        )
        text_a = MathTex("a").next_to(triangle, LEFT)
        text_b = MathTex("b").next_to(triangle, DOWN)
        text_c = MathTex("c").next_to([b / 2, a / 2, 0], (UP + RIGHT) / np.sqrt(2))

        tri_and_text = VGroup(triangle, text_a, text_b, text_c)
        self.play(Create(triangle))
        self.play(FadeIn(text_a, text_b, text_c))
        self.play(tri_and_text.animate.shift((a + b) / 2 * (LEFT + DOWN)))
        self.next_slide()
        # square over the hypotenuse
        csquare = Square(c, color=colourcomp, **common_kwargs).rotate(np.arctan(b / a))
        text_c2 = text_c.copy()
        self.play(Create(csquare), Transform(text_c2, MathTex("c^2")))
        self.next_slide()
        # triangles of the sides of the squares
        triangle2 = triangle.copy()
        self.play(triangle2.animate.rotate_about_origin(90 * DEGREES))
        triangle3 = triangle2.copy()
        self.play(triangle3.animate.rotate_about_origin(90 * DEGREES))
        triangle4 = triangle3.copy()
        self.play(triangle4.animate.rotate_about_origin(90 * DEGREES))
        # remember for later
        div_one = VGroup(
            triangle.copy(),
            triangle2.copy(),
            triangle3.copy(),
            triangle4.copy(),
            csquare,
            text_c2,
        )
        self.next_slide()
        # big square
        bigsquare = Square(a + b, color=coloursec1)
        self.play(FadeIn(bigsquare))

        # text
        text_adown = MathTex("a").next_to(triangle2, DOWN)
        text_bleft = MathTex("b").next_to(triangle4, LEFT)
        text_leftdown = VGroup(text_adown, text_bleft)
        text_rightup = VGroup(
            MathTex("b").next_to(triangle2, RIGHT),
            MathTex("a").next_to(triangle3, RIGHT),
            MathTex("b").next_to(triangle3, UP),
            MathTex("a").next_to(triangle4, UP),
        )
        self.play(FadeIn(text_leftdown, text_rightup, lag_ratio=1.1))

        # self.wait(2)
        self.next_slide()

        # rearrange triangles, delete square
        self.play(
            triangle2.animate.rotate(
                90 * DEGREES, about_point=[-(a + b) / 2 + b, -(a + b) / 2, 0]
            ),
            triangle3.animate.rotate(
                -90 * DEGREES, about_point=[-(a + b) / 2 + a, (a + b) / 2, 0]
            ),
            FadeOut(csquare),
            FadeOut(text_c2),
            FadeOut(text_rightup),
        )
        rect = VGroup(triangle3, triangle4)
        self.play(rect.animate.shift([b, 0, 0]))

        self.next_slide()
        # small squares
        asquare = Square(a, color=colourcomp, **common_kwargs).shift([b / 2, -b / 2, 0])
        bsquare = Square(b, color=colourcomp, **common_kwargs).shift([-a / 2, a / 2, 0])
        self.play(Create(asquare), Create(bsquare))
        text_a2 = text_adown.copy()
        text_b2 = text_bleft.copy()
        self.play(
            Transform(text_a2, MathTex("a^2").shift(asquare.get_center())),
            Transform(text_b2, MathTex("b^2").shift(bsquare.get_center())),
        )
        #
        self.next_slide()
        div_two = VGroup(
            triangle,
            triangle2,
            triangle3,
            triangle4,
            asquare,
            bsquare,
            text_a2,
            text_b2,
        )
        self.play(
            FadeOut(text_a, text_b, text_c, bigsquare, text_adown, text_bleft),
            FadeIn(div_one),
            div_one.animate.shift((a + b) / 2 * LEFT),
            div_two.animate.shift((a + b) / 2 * RIGHT),
        )
        self.play(ScaleInPlace(div_one, 0.7), ScaleInPlace(div_two, 0.7))
