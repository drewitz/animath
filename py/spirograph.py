from manim import *
import numpy as np


def spiro_curve(
    r: int = 2, R: int = 3, d: float = 0.618, scale: float = 1, resolution: int = 1000
):
    """
    returns locations of drawing point in a spirograph setting.
    r and R are ideally coprime
    0<d<1 (for a physically sensible solution. other values should still work)
    """
    ratio = r / R
    phi = np.linspace(0, 2 * np.pi * R, resolution)
    s_phi = (1 - R / r) * phi
    dest = (1 - ratio) * np.array([np.cos(phi), np.sin(phi)]) + d * ratio * np.array(
        [np.cos(s_phi), np.sin(s_phi)]
    )

    return dest

def get_ax_with_spiro(
        r: int = 2, R: int=3, scale: float = 1, resolution: int = 1000
        ):
    ax = Axes(x_range=[-1.5, 1.5, 0.5], y_range=[-1.5, 1.5, 0.5], x_length=4, y_length=4)
    curves = VGroup()
    for d in np.linspace(0.1, 0.9, 9):
        curve = VMobject().set_points_as_corners(ax.c2p(spiro_curve(r=r, R=R, d=d, scale = scale, resolution=resolution).T))
        curve.set_stroke(BLUE*d + GREEN*(1-d), 2)
        curves.add(curve)
    return ax, curves


class Spirograph(Scene):
    def construct(self):
        axs = VGroup()
        curvesgrp = VGroup()
        for i in range(1, 5):
            ax, curves = get_ax_with_spiro(r=i, R=5)
            axs.add(ax)
            curvesgrp.add(curves)
        curvesgrp.arrange()

        self.play(*[Create(curves, run_time=10, rate_func=linear) for curves in curvesgrp])
        self.wait()
