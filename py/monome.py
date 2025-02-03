from manim import *
from manim_slides import Slide


class Potenz(Slide):
    """drawing an animation of the Newton method"""

    n_max = 9

    def construct(self):
        ax = Axes().add_coordinates()
        ax_labels = ax.get_axis_labels()
        self.add(ax, ax_labels)
        text = MathTex("f(x) = \ldots").shift(4 * RIGHT + 2 * UP)
        self.add(text)

        graph = None
        for n in range(self.n_max):
            newtext = MathTex(f"f(x) = x^{{{n}}}").shift(text.get_center())
            if graph is not None:
                new_graph = ax.plot(lambda x: x**n, x_range=[-2, 2], color="blue")

                self.play(Transform(graph, new_graph), Transform(text, newtext))
                # graph = new_graph
            else:
                graph = ax.plot(lambda x: x**n, color="blue")
                self.play(FadeIn(graph), Transform(text, newtext))
            self.next_slide()

        self.play(FadeOut(graph))
        self.next_slide()

        graph = None
        for n in range(self.n_max):
            newtext = MathTex(f"f(x) = x^{{{-n}}}").shift(text.get_center())
            if graph is not None:
                new_graph = VGroup(
                    ax.plot(
                        lambda x: x ** (-n),
                        x_range=[-6, -(0.1 ** (1 / n))],
                        color="blue",
                    ),
                    ax.plot(
                        lambda x: x ** (-n), x_range=[0.1 ** (1 / n), 6], color="blue"
                    ),
                )

                self.play(Transform(graph, new_graph), Transform(text, newtext))
                # graph = new_graph
            else:
                graph = VGroup(
                    ax.plot(lambda x: x ** (-n), x_range=[-6, -0.01], color="blue"),
                    ax.plot(lambda x: x ** (-n), x_range=[0.01, 6], color="blue"),
                )
                self.play(FadeIn(graph), Transform(text, newtext))
