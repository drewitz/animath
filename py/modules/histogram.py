from manim import *
import numpy as np

from collections.abc import Iterable, MutableSequence


class Histogram(Axes):
    """Creates a histogram. Similar to :class:`~.BarChart` but should have a more flexible x-axis.

    Parameters
    ----------
    xs
        A sequence of values that determines the left and right bounds of each bar.
    values
        A sequence of heights for each bar. Should match the length of ``xs`` minus 1.
    bar_colors
        The color for the bars. Accepts a sequence of colors (can contain just one item).
        If the length of``bar_colors`` does not match that of ``values``,
        intermediate colors will be automatically determined.
    bar_fill_opacity
        The fill opacity of the bars.
    bar_stroke_width
        The stroke width of the bars.
    """

    def __init__(
        self,
        xs: MutableSequence[float],
        values: MutableSequence[float],
        bar_colors: Iterable[str] = [
            "#003f5c",
            "#58508d",
            "#bc5090",
            "#ff6361",
            "#ffa600",
        ],
        bar_fill_opacity: float = 0.7,
        bar_stroke_width: float = 3,
        x_range=None,
        y_range=None,
        **kwargs
    ):
        self.xs = xs
        self.values = values
        self.bar_colors = bar_colors
        self.bar_fill_opacity = bar_fill_opacity
        self.bar_stroke_width = bar_stroke_width
        self.bars = VGroup()
        if x_range is None:
            x_range = [min(xs), max(xs)]
        if y_range is None:
            y_range = [min([0, min(values)]), max([0, max(values)])]
        # this shouldn't be necessary?
        # x_range[1] += 0.1*(x_range[1]-x_range[0])  # tip shouldn't interfere with bars
        # y_range[1] += 0.1*(y_range[1]-y_range[0])
        super().__init__(x_range=x_range, y_range=y_range, **kwargs)
        self._add_bars()

    def update_bars(
        self,
        xs: MutableSequence[float] | None = None,
        values: MutableSequence[float] | None = None,
    ):
        self.remove(self.bars)
        self.bars = VGroup()
        if xs is not None:
            self.xs = xs
        if values is not None:
            self.values = values
        self._add_bars()

    def _add_bars(self) -> None:
        for i, value in enumerate(self.values):
            tmpbar = self._create_bar(*self.xs[i : i + 2], value)
            self.bars.add(tmpbar)

        self._update_colors()
        self.add_to_back(self.bars)

    def _create_bar(self, left, right, height) -> Rectangle:
        bar_h = self.c2p(0, abs(height))[1] - self.c2p(0, 0)[1]
        bar_w = self.c2p(right, 0)[0] - self.c2p(left, 0)[0]
        bar = Rectangle(
            width=bar_w,
            height=bar_h,
            stroke_width=self.bar_stroke_width,
            fill_opacity=self.bar_fill_opacity,
        )
        pos = UP if (height >= 0) else DOWN
        bar.next_to(self.c2p(0.5 * (right + left), 0), pos, buff=0)
        return bar

    def _update_colors(self):
        """Initialize the colors of the bars of the chart.

        Sets the color of ``self.bars`` via ``self.bar_colors``.

        Primarily used when the bars are initialized with ``self._add_bars``
        or updated via ``self.change_bar_values``.
        """
        self.bars.set_color_by_gradient(*self.bar_colors)


class HistTest(Scene):
    def construct(self):
        xmin, xmax = (-5, 5)
        xs = np.linspace(xmin, xmax, 11)
        mids = np.array([np.mean(xs[i : i + 2]) for i in range(len(xs) - 1)])
        ys = np.exp(-(mids**2) / 2) / np.sqrt(2 * np.pi)
        hist = Histogram(xs, ys, x_range=[-5.5, 5.5, 1], y_range=[0, 0.5, 0.1])
        for n_bars in [10, 20, 40, 80, 160, 320]:
            xs = np.linspace(xmin, xmax, n_bars + 1)
            mids = np.array([np.mean(xs[i : i + 2]) for i in range(len(xs) - 1)])
            ys = np.exp(-(mids**2) / 2) / np.sqrt(2 * np.pi)
            self.play(hist.animate.update_bars(xs, ys))
        t = np.linspace(xmin, xmax, 500)
        yt = np.exp(-(t**2) / 2) / np.sqrt(2 * np.pi)
        graph = hist.plot_line_graph(t, yt, add_vertex_dots=False, line_color=BLUE)
        self.play(FadeIn(graph))
        self.wait()
