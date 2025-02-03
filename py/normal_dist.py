import numpy as np
from scipy.special import comb
from manim import *
from manim_slides import Slide
from modules.histogram import Histogram
from modules.samples import DeterministicSample


class BinomialDist(Slide):
    p = 0.4
    q = 1 - p

    def get_prob(self, k, n):
        return comb(n, k) * self.p**k * self.q ** (n - k)

    def get_histogram(self, n, **kwargs):
        xs = np.arange(n + 1)
        probs = np.array([self.get_prob(k, n) for k in xs])
        bounds = np.arange(n + 2) - 0.5
        return Histogram(bounds, probs, **kwargs)

    def construct(self):
        hists = VGroup()
        kwargs = {
            "x_range": [-10, 40, 5],
            "y_range": [0, 0.45, 0.1],
        }
        axes_config = {
            "x_axis_config": {"include_numbers": True},
            "y_axis_config": {"include_numbers": True},
        }
        ns = [10, 20, 30, 40, 50, 60]
        for n, histcol in zip(ns, [RED, PURPLE, BLUE, GREEN, YELLOW, ORANGE]):
            newhist = self.get_histogram(
                n, bar_colors=[histcol], **kwargs, **axes_config
            )
            self.play(FadeIn(newhist))
            hists.add(newhist)
            self.next_slide()

        for i, hist in enumerate(hists):
            newxs = hist.xs - ns[i] * self.p
            newvalues = hist.values
            self.play(hist.animate.update_bars(newxs, newvalues))

        self.next_slide()

        for i, hist in enumerate(hists):
            std = np.sqrt(ns[i] * self.p * self.q)
            newxs = hist.xs / std
            newvalues = hist.values * std
            self.play(hist.animate.update_bars(newxs, newvalues))

        self.next_slide()
        newhists = [
            Histogram(
                h.xs,
                h.values,
                h.bar_colors,
                x_range=[-3, 3, 0.5],
                y_range=kwargs["y_range"],
                **axes_config
            )
            for h in hists
        ]
        self.play(*[ReplacementTransform(h, hnew) for h, hnew in zip(hists, newhists)])
        graph = newhists[-1].plot(lambda x: np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi))
        self.play(FadeIn(graph))


class NormalDist(Slide):
    def construct(self):
        trial = DeterministicSample()

        # title = Tex(r"What happens if we increase\\the sample size\\and the number of bins?")
        # self.play(FadeIn(title))
        # self.next_slide()

        xmin = -5
        xmax = 5
        xstep = 1
        x_range = [xmin, xmax, xstep]
        axis_config = {
            # "include_tip": True
            "include_numbers": True
        }
        counts, names = trial.get_bins(xmin=xmin, xmax=xmax, n_bins=25)
        bounds = np.linspace(xmin, xmax, 26)
        hist = Histogram(
            bounds,
            counts,
            # names,
            x_range=x_range,
            y_range=[0, 0.5, 0.1],
            x_axis_config=axis_config,
            y_axis_config=axis_config,
        )

        for k in [50, 100, 200, 400]:
            counts, names = trial.get_bins(xmin=xmin, xmax=xmax, n_bins=k)
            bounds = np.linspace(xmin, xmax, k + 1)

            self.play(hist.animate.update_bars(bounds, counts))
            self.next_slide()

        self.next_slide()
        # doesnt work???
        graph = hist.plot(lambda x: trial.pdf(x))
        self.play(FadeIn(graph))
