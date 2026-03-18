from manim import *
from manim_slides import Slide
import numpy as np


# PARAMETERS

r = 2
angle = np.pi * 2.3 / 5
rt = 3

# colours
colour_tri = "#5be800"
colour_quad = "#0777ba"
colour_square_b = "#bf0603"

common_kwargs = {"fill_opacity": 0.5}


class Kathetensatz(Slide):
    def construct(self):
        ##############################
        # SETUP
        ##############################
        # vertices of the triangle
        pa = np.array([-r, 0, 0])
        pb = np.array([r, 0, 0])
        pc = np.array([r * np.cos(angle), r * np.sin(angle), 0])
        # side lengths
        a = np.sqrt((pc[0] - pb[0]) ** 2 + pc[1] ** 2)
        b = np.sqrt(4 * r**2 - a**2)
        triangle = Polygon(pa, pb, pc, color=colour_tri, **common_kwargs)

        # square over a
        a_tracker = ValueTracker(0)
        p1 = pb
        p2 = pb + a * np.array([np.cos(angle / 2), np.sin(angle / 2), 0])
        p3_0 = p2 + pc - pb
        p4_0 = pc
        square_a = Polygon(p1, p2, p3_0, p4_0, color=colour_quad, **common_kwargs)
        square_a_copy = square_a.copy()
        square_a_copy.set(fill_opacity=0.1)

        # square over b
        b_tracker = ValueTracker(0)
        p2b = pa + b * np.array([-np.sin(angle / 2), np.cos(angle / 2), 0])
        p3b_0 = p2b + pc - pa
        p4b_0 = pc
        square_b = Polygon(
            pa, p2b, p3b_0, p4b_0, color=colour_square_b, **common_kwargs
        )
        square_b_copy = square_b.copy()
        square_b_copy.set(fill_opacity=0.1)

        # text
        text_a2 = MathTex("a^2").shift(square_a.get_center())
        text_b2 = MathTex("b^2").shift(square_b.get_center())

        self.play(
            FadeIn(triangle),
            FadeIn(square_a),
            FadeIn(square_b),
            FadeIn(square_a_copy),
            FadeIn(square_b_copy),
        )
        self.play(FadeIn(text_a2), FadeIn(text_b2))
        self.next_slide()

        ##############################
        # ANIMATE SQUARE A
        ##############################

        # animation updater
        # square_a
        square_a.add_updater(
            lambda x: x.become(
                Polygon(
                    p1,
                    p2,
                    p3_0 + (pa - pc) * a_tracker.get_value(),
                    p4_0 + (pa - pc) * a_tracker.get_value(),
                    color=colour_quad,
                    **common_kwargs
                )
            )
        )
        self.play(a_tracker.animate.increment_value(1), run_time=rt)
        self.next_slide()

        angle_tracker = ValueTracker(0)
        p4 = pa
        p3 = p4 + p2 - p1
        p3d = p3 - p1
        square_a.add_updater(
            lambda x: x.become(
                Polygon(
                    pb,
                    pb
                    + a
                    * np.array(
                        [
                            np.cos(angle / 2 + angle_tracker.get_value()),
                            np.sin(angle / 2 + angle_tracker.get_value()),
                            0,
                        ]
                    ),
                    p1
                    + np.array(
                        [
                            p3d[0] * np.cos(angle_tracker.get_value())
                            - p3d[1] * np.sin(angle_tracker.get_value()),
                            p3d[0] * np.sin(angle_tracker.get_value())
                            + p3d[1] * np.cos(angle_tracker.get_value()),
                            0,
                        ]
                    ),
                    pb
                    + 2
                    * r
                    * np.array(
                        [
                            -np.cos(angle_tracker.get_value()),
                            -np.sin(angle_tracker.get_value()),
                            0,
                        ]
                    ),
                    color=colour_quad,
                    **common_kwargs
                )
            )
        )
        self.play(angle_tracker.animate.increment_value(np.pi / 2), run_time=rt)
        self.next_slide()

        p2 = pc
        p3 = pc + np.array([0, -2 * r, 0])
        p4 = p1 + np.array([0, -2 * r, 0])

        s_tracker = ValueTracker(0)
        square_a.add_updater(
            lambda x: x.become(
                Polygon(
                    p1,
                    p2 * np.array([1, 1 - s_tracker.get_value(), 1]),
                    p2 * np.array([1, 1 - s_tracker.get_value(), 1])
                    - np.array([0, 2 * r, 0]),
                    p4,
                    color=colour_quad,
                    **common_kwargs
                )
            )
        )
        self.play(s_tracker.animate.increment_value(1), run_time=rt)

        text_pa = MathTex("pa").shift(square_a.get_center())
        self.play(FadeIn(text_pa))
        self.next_slide()

        ##############################
        # ANIMATE SQUARE B
        ##############################
        # animation updater
        # square_b
        square_b.add_updater(
            lambda x: x.become(
                Polygon(
                    pa,
                    p2b,
                    p3b_0 + (pb - pc) * b_tracker.get_value(),
                    p4b_0 + (pb - pc) * b_tracker.get_value(),
                    color=colour_square_b,
                    **common_kwargs
                )
            )
        )
        self.play(b_tracker.animate.increment_value(1), run_time=rt)
        self.next_slide()

        # rotate parallelogram
        angle_tracker_b = ValueTracker(0)
        p4b = pb
        p3db = p2b + pb - 2 * pa  # direction of the third point as seen from pa...
        square_b.add_updater(
            lambda x: x.become(
                Polygon(
                    pa,
                    pa
                    + b
                    * np.array(
                        [
                            -np.sin(angle / 2 - angle_tracker_b.get_value()),
                            np.cos(angle / 2 - angle_tracker_b.get_value()),
                            0,
                        ]
                    ),
                    pa
                    + np.array(
                        [
                            p3db[0] * np.cos(-angle_tracker_b.get_value())
                            - p3db[1] * np.sin(-angle_tracker_b.get_value()),
                            p3db[0] * np.sin(-angle_tracker_b.get_value())
                            + p3db[1] * np.cos(-angle_tracker_b.get_value()),
                            0,
                        ]
                    ),
                    pa
                    + 2
                    * r
                    * np.array(
                        [
                            np.cos(-angle_tracker_b.get_value()),
                            np.sin(-angle_tracker_b.get_value()),
                            0,
                        ]
                    ),
                    color=colour_square_b,
                    **common_kwargs
                )
            )
        )
        self.play(angle_tracker_b.animate.increment_value(np.pi / 2), run_time=rt)
        self.next_slide()

        p2b = pa + np.array([0, -2 * r, 0])
        p3b = pc + np.array([0, -2 * r, 0])
        p4b = pc

        s_tracker_b = ValueTracker(0)
        square_b.add_updater(
            lambda x: x.become(
                Polygon(
                    pa,
                    p2b,
                    p4b * np.array([1, 1 - s_tracker_b.get_value(), 1])
                    - np.array([0, 2 * r, 0]),
                    p4b * np.array([1, 1 - s_tracker_b.get_value(), 1]),
                    color=colour_square_b,
                    **common_kwargs
                )
            )
        )
        self.play(s_tracker_b.animate.increment_value(1), run_time=rt)

        # text q*b
        text_qb = MathTex("qb").shift(square_b.get_center())
        self.play(FadeIn(text_qb))
        # text_pc = MathTex("pc").shift(square_a.get_center())
        # self.play(FadeIn(text_pc), FadeIn(text_eq))
