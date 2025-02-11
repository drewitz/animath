from manim import *
from manim_slides import Slide
import numpy as np

COLOUR_X = PURPLE
COLOUR_Y = YELLOW


class LGS(Slide):
    def construct(self):
        # setup  equations
        a1 = 3
        b1 = 4
        c1 = 8
        a2 = -3
        b2 = 6
        c2 = 6
        # create first equation
        # TODO: maybe show second equation as well in the beginning?
        t2c = {
            "x": COLOUR_X,
            "y": COLOUR_Y,
        }
        both_og_eqns = MathTex(f"{a1}\,x + {b1}\,y & = {c1} \\\\", f"{a2}\,x + {b2}\,y & = {c2}", tex_to_color_map=t2c)
        eqn1 = MathTex(f"{a1}\,x + {b1}\,y & = {c1}", tex_to_color_map=t2c)
        # eqn1b = MathTex(f"y = -\\frac{{ {a1} }}{{ {b1 } }}\,x + \\frac{{ {c1} }}{{ {b1 } }}", tex_to_color_map=t2c)
        eqn1step = MathTex(f"{b1}\,y=-{a1}\,x + {c1}", tex_to_color_map=t2c)
        eqn1b = MathTex(f"y = -{a1/b1}\,x + {c1/b1}", tex_to_color_map=t2c)
        self.play(Write(both_og_eqns))
        self.next_slide()
        self.play(TransformMatchingTex(both_og_eqns, eqn1))
        self.next_slide()
        self.play(TransformMatchingTex(eqn1, eqn1step, path_arc=PI/2))
        self.next_slide()
        self.play(TransformMatchingTex(eqn1step, eqn1b, path_arc=PI/2))
        self.next_slide()
        # move equation to the right and create graph
        xmin, xmax = 0, 5
        xs = np.linspace(xmin-0.2, xmax, 10)
        ax = Axes(x_range=[xmin, xmax, 1], y_range=[0, 5, 1], x_axis_config={"color": COLOUR_X}, y_axis_config={"color": COLOUR_Y}, x_length=6, y_length=6).next_to((0, 0, 0), LEFT, buff=0.5)
        f = lambda x: -x*a1/b1 + c1/b1
        line = ax.plot_line_graph(xs, f(xs), add_vertex_dots=False, line_color=BLUE)

        self.play(eqn1b.animate.next_to((0, 0, 0), RIGHT, buff=0.5))
        self.play(FadeIn(ax))
        self.play(FadeIn(line))
        # insert point
        x = ValueTracker()
        pt1 = always_redraw(
            lambda:
            Dot(ax.c2p(x.get_value(), f(x.get_value()), 0), color=WHITE)
        )
        def get_eqn_with_xy():
            dest = MathTex(f"{np.round(f(x.get_value()), 2)}", f" = {-a1/b1}\cdot", np.round(x.get_value(), 2), f"+ {c1/b1}").move_to(eqn1b.get_center())
            dest[0].set_color(COLOUR_Y)
            dest[2].set_color(COLOUR_X)
            return dest
        eqn1xyreplaced = always_redraw(
            get_eqn_with_xy
        )
        self.next_slide()
        self.play(FadeIn(pt1), ReplacementTransform(eqn1b, eqn1xyreplaced))
        self.next_slide()
        self.play(x.animate.set_value(3), run_time=5)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait(2)
        self.play(x.animate.set_value(3.5), run_time=5)
        self.next_slide()
        # second equation
        g = lambda x: -x*a2/b2 + c2/b2
        pt2 = always_redraw(
            lambda:
            Dot(ax.c2p(x.get_value(), g(x.get_value()), 0), color=WHITE)
        )
        #def get_eqn2_with_xy():
        #    dest = MathTex(f"{np.round(g(x.get_value()), 2)}", f" = {-a2/b2}\cdot", np.round(x.get_value(), 2), f"+ {c2/b2}").next_to(eqn1b, DOWN)
        #    dest[0].set_color(COLOUR_Y)
        #    dest[2].set_color(COLOUR_X)
        #    return dest

        def get_both_eqn_with_xy():
            dest = MathTex(f"{np.round(f(x.get_value()), 2)}", f" & = {-a1/b1}\cdot", np.round(x.get_value(), 2), f"+ {c1/b1}\\\\",
                f"{np.round(g(x.get_value()), 2)}", f" & = {-a2/b2}\cdot", np.round(x.get_value(), 2), f"+ {c2/b2}").move_to(eqn1b.get_center())
            dest[0].set_color(COLOUR_Y)
            dest[2].set_color(COLOUR_X)
            dest[4].set_color(COLOUR_Y)
            dest[6].set_color(COLOUR_X)
            return dest
        both_eqns = always_redraw(
            get_both_eqn_with_xy
        )
        line2 = ax.plot_line_graph(xs, g(xs), add_vertex_dots=False, line_color=GREEN)
        eqn2 = MathTex(f"y = {-a2/b2}\,x +  {c2/b2}", tex_to_color_map=t2c).next_to(eqn1b, DOWN)
        self.play(FadeIn(line2), Write(eqn2))
        self.next_slide()
        self.play(FadeIn(pt2), FadeOut(eqn2), ReplacementTransform(eqn1xyreplaced, both_eqns))
        # find intersection
        self.next_slide()
        intersection_x = (c1/b1 - c2/b2)/(a1/b1 - a2/b2)
        self.play(x.animate.set_value(intersection_x), run_time=3)

        solution = MathTex(f"L = \\left\\{{ ( 0.8 \\mid 1.4 ) \\right\\}}").next_to(both_eqns, DOWN, buff=1)
        self.play(Write(solution))

