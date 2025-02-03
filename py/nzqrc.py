from manim import *
from manim_slides import Slide
import numpy as np


# PARAMETERS

dist = 1
long = 10  # wait
short = 3  # wait
supershort = short / 2

# colours
colN = BLUE
colZ = YELLOW
colQ = GREEN
colR = RED
colC = PURPLE

common_kwargs = {"fill_opacity": 0.5}


class Numbersets(Slide):
    # SCENE
    # global parameters of the thing
    nmax = 5
    levelQ = 30
    thelag = 0.5
    dotsN = []
    dotsZ = []
    dotsQ = []
    dotsR = []

    def appearN(self):
        self.nl = NumberLine(
            x_range=[0, self.nmax, 1],
            include_numbers=True,
            exclude_origin_tick=True,
            include_tip=True,
        ).shift(self.nmax / 2 * RIGHT)
        self.play(Create(self.nl))

        self.dotsN = VGroup(*[Dot(x * RIGHT, color=colN) for x in range(1, self.nmax)])
        self.play(Create(self.dotsN), lag_ratio=self.thelag)

    def appearZ(self):
        self.nlZ = NumberLine(
            x_range=[-self.nmax + 0.01, self.nmax, 1],
            include_numbers=True,
            include_tip=True,
            numbers_to_exclude=[-self.nmax],
        )
        self.play(FadeOut(self.nl), FadeIn(self.nlZ))
        self.dotsZ = VGroup(*[Dot(x * LEFT, color=colZ) for x in range(self.nmax)])
        self.play(Create(self.dotsZ), lag_ratio=self.thelag)
        self.play(FadeToColor(self.dotsN, colZ), FadeIn(self.textZ))

    def appearQ(self):
        self.labelsQ = []
        old = None
        for k in range(2, self.levelQ + 1):
            indices = range(-self.nmax * k, self.nmax * k + 1)
            newdots = [Dot(i / k * RIGHT, color=colQ).scale(0.5) for i in indices]
            labeldownshift = 1.5 * UP
            newlabels = (
                [MathTex(r"\cdots").shift(labeldownshift + self.nmax * LEFT)]
                + [
                    MathTex(rf"\frac{{{i}}}{{{k}}}", color=colQ).shift(
                        labeldownshift + i * RIGHT
                    )
                    for i in indices
                    if abs(i) < self.nmax
                ]
                + [MathTex(r"\cdots").shift(labeldownshift + self.nmax * RIGHT)]
            )
            heightshift = (newlabels[1].height / 2 + 0.1) * DOWN
            newlines = [
                DashedLine(i / k * RIGHT, heightshift + labeldownshift + i * RIGHT)
                for i in indices
                if abs(i) < self.nmax
            ]
            if old is None:
                old = VGroup(*newdots, *newlabels, *newlines)
                self.play(Create(old))
            else:
                new = VGroup(*newdots, *newlabels, *newlines)
                # self.play(Transform(old, new))
                self.play(FadeOut(old), FadeIn(new), run_time=1 / (k - 1))
                old = new
            # self.wait(supershort)
        self.play(FadeOut(VGroup(*newlabels, *newlines)), FadeIn(self.textQ))
        self.dotsQ = newdots

    def appearR(self):
        thevalue = ValueTracker(0)

        def update_label(mobj):
            mobj.set_value(self.dotR.get_center()[0])
            mobj.next_to(self.dotR, UP)

        def update_dot(mobj):
            mobj.move_to(self.nl.n2p(thevalue.get_value()))

        self.dotR = Dot(color=colR)
        self.labelR = DecimalNumber(
            0, num_decimal_places=4, color=colR, show_ellipsis=True
        ).next_to(self.dotR, UP)
        self.labelR.add_updater(update_label)
        self.dotR.add_updater(update_dot)
        self.add(self.dotR)

        # self.add(self.dotR, self.labelR)
        # animate the movement
        def next_point(newval, newlab):
            self.play(thevalue.animate.set_value(newval), FadeIn(self.labelR))
            newtext = MathTex(newlab, color=colR).move_to(self.labelR.get_center())
            newdot = Dot(self.dotR.get_center(), color=colR)
            self.dotsR += [newdot]
            self.play(FadeOut(self.labelR), FadeIn(newtext), FadeIn(newdot))

        # to pi
        for x in [
            (np.pi, r"\pi"),
            (-np.e, r"-\mathrm{e}"),
            (np.sqrt(2), r"\sqrt{2}"),
            (0.5 * (-np.sqrt(5) + 1), r"1-\varphi"),
        ]:
            next_point(*x)
            self.wait(supershort)

        newline = self.nlZ.copy().set_color(colR)
        self.play(FadeOut(self.dotR), Transform(self.nlZ, newline), FadeIn(self.textR))

    def appearC(self):
        real = ValueTracker(0)
        imag = ValueTracker(0)

        def update_label(mobj):
            mobj.set_value(
                rf"{self.dotC.get_center()[0]}+{self.dotC.get_center()[1]}\cdot\mathrm{{i}}"
            )
            mobj.next_to(self.dotC, UP)

        def update_dot(mobj):
            mobj.move_to(real.get_value() * RIGHT + imag.get_value() * UP)

        self.dotC = Dot(color=colC)
        self.labelC = MathTex(rf"0", color=colC).next_to(self.dotC, UP)
        self.labelC.add_updater(update_label)
        self.dotC.add_updater(update_dot)
        self.add(self.dotC, self.labelC)
        self.play(real.animate.set_value(1))
        self.play(imag.animate.set_value(1))

    def construct(self):
        # Text
        self.textN = Tex(r"$\mathbb{N}$", color=colN)
        self.textZ = Tex(r"$\subset \mathbb{Z}$", color=colZ).next_to(self.textN, RIGHT)
        self.textQ = Tex(r"$\subset \mathbb{Q}$", color=colQ).next_to(self.textZ, RIGHT)
        self.textR = Tex(r"$\subset \mathbb{R}$", color=colR).next_to(self.textQ, RIGHT)
        self.textall = VGroup(self.textN, self.textZ, self.textQ, self.textR)
        self.textall.shift(
            (self.textN.width - self.textall.width) / 2 * RIGHT
            + config.frame_height * 3 / 8 * DOWN
        )
        # Animation
        self.appearN()
        self.play(FadeIn(self.textN))
        self.next_slide()

        self.appearZ()
        self.next_slide()

        self.appearQ()
        # self.wait(supershort)

        self.play(FadeOut(VGroup(self.dotsN, self.dotsZ, *self.dotsQ)))
        self.next_slide()

        self.appearR()
