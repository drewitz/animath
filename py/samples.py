import numpy as np


class Sample:
    def __init__(self, sample):
        self.sample = sample
        self.n = len(sample)

    def get_bins(self, xmin, xmax, n_bins=None, dx=None):
        if dx is None:
            if n_bins is None:
                n_bins = np.floor(np.sqrt(self.n))
        else:
            if n_bins is not None:
                raise ValueError(
                    "Only one of n_bins or dx can be given as an argument."
                )
            n_bins = int((xmax - xmin) / dx)

        bounds = np.linspace(xmin, xmax, n_bins + 1)
        counts = np.array(
            [
                len(
                    np.argwhere(
                        np.logical_and(
                            self.sample > bounds[i], self.sample < bounds[i + 1]
                        )
                    )
                )
                for i in range(n_bins)
            ]
        )
        names = [
            np.round(np.mean(bounds[i : i + 2]), decimals=1) for i in range(n_bins)
        ]
        bin_width = (xmax - xmin) / n_bins
        heights = counts / bin_width / self.n
        self.counts = counts
        return heights, names

    def get_int_bins(self, xmin=None, xmax=None):
        if xmin is None:
            xmin = np.floor(min(self.sample))
        if xmax is None:
            xmax = np.ceil(max(self.sample))
        return self.get_bins(xmin, xmax, dx=1)


# Should this inherit from Sample?
# Does it make sense at all?
class DeterministicSample:
    def __init__(self, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        return np.exp(-((x - self.mu) ** 2) / (2 * self.sigma**2)) / np.sqrt(
            2 * np.pi * self.sigma**2
        )

    def get_bins(self, xmin, xmax, n_bins=None, dx=None):
        if dx is None:
            if n_bins is None:
                n_bins = np.floor(np.sqrt(self.n))
        else:
            if n_bins is not None:
                raise ValueError(
                    "Only one of n_bins or dx can be given as an argument."
                )
            n_bins = int((xmax - xmin) / dx)

        bounds = np.linspace(xmin, xmax, n_bins + 1)
        names = np.array([np.mean(bounds[i : i + 2]) for i in range(n_bins)])
        heights = self.pdf(names)
        return heights, names


class RandomSample(Sample):
    def __init__(self, n=100, mu=0, sigma=1):
        rng = np.random.default_rng()
        self.mu = mu
        self.sigma = sigma
        sample = rng.normal(mu, sigma, size=n)
        super().__init__(sample)
