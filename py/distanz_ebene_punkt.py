from manim import *
from manim_slides import Slide


class DistanzEbenePunkt(Slide):
    def construct(self):
        width = 4
        height = 1
        # tex to colour
        t2c = {
            r"\overrightarrow{n}": GREEN,
            "E": BLUE,
            "P": PURPLE,
            "S": RED,
            #"g": YELLOW,
        }
        # stuff
        plane = Polygon(
            [width + height / 2, height, 0],
            [height / 2 - width, height, 0],
            [-height / 2 - width, -height, 0],
            [-height / 2 + width, -height, 0],
            fill_color=BLUE,
            fill_opacity=0.5,
        ).shift(0.8*DOWN)
        plane.z_index = 1
        px = 2.5
        py = 2
        punktp = Dot([px, py, 0], color=PURPLE).shift(0.8*DOWN)
        punktp.z_index = 3
        punkts = Dot([px, height / 3, 0], color=RED).shift(0.8*DOWN)
        punkts.z_index = 3
        gerade_oben = Line([px, py + 3, 0], [px, height / 3, 0], color=YELLOW).shift(
            0.8*DOWN
        )
        gerade_oben.z_index = 2
        gerade_dashed = DashedLine(
            [px, height / 3, 0], [px, -height, 0], color=YELLOW
        ).shift(0.8*DOWN)
        gerade_unten = Line([px, -height, 0], [px, -2 * height, 0], color=YELLOW).shift(
            0.8*DOWN
        )
        gerade = VGroup(gerade_oben, gerade_dashed, gerade_unten)
        vectorn = Arrow(DOWN, UP, color=GREEN).shift(width / 2 * LEFT)
        vectorn.z_index = 3
        secondvector = Arrow(DOWN, UP, color=GREEN).next_to(punktp, UP, buff=0)
        # tex
        planeeq = MathTex(r"E:\begin{pmatrix}x\\y\\z\end{pmatrix}\bullet\overrightarrow{n}=d", tex_to_color_map=t2c).next_to(plane, DOWN, aligned_edge=LEFT)
        vecname = MathTex(r"\overrightarrow{n}", color=GREEN).next_to(vectorn, UP)
        pname = MathTex("P", color=PURPLE).next_to(punktp, RIGHT + UP)
        pname.z_index = 3
        sname = MathTex("S", color=RED).next_to(punkts, RIGHT + DOWN)
        sname.z_index = 3
        lineeq = MathTex(
            r"g:\overrightarrow{OP} + t\cdot\overrightarrow{n}"
        ).next_to(gerade, LEFT).to_edge(UP)
        #self.add(index_labels(lineeq[0]))
        lineeq[0][0].set_color(YELLOW)
        lineeq[0][2:7].set_color(PURPLE)
        lineeq[0][-2:].set_color(GREEN)

        # slides
        self.play(Create(plane), Write(planeeq[0]))
        self.next_slide()
        self.play(Write(planeeq[1:]), Create(vectorn), Write(vecname))
        self.next_slide()
        self.play(FadeIn(punktp), Write(pname))
        self.next_slide()
        self.play(ReplacementTransform(vectorn.copy(), secondvector))
        self.next_slide()
        self.play(GrowFromPoint(gerade, [px, py + 1, 0], GREEN))
        self.play(Write(lineeq))
        self.next_slide()
        self.play(FadeIn(punkts), Write(sname))
