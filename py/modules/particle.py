"""Particle module

Particle class
meant for moving particles or 'people'
"""

from tkinter import N
import numpy as np

class Particle:
    """describes a moving particle
    
    should be able to move and bump into things.
    """
    xmin = 0
    xmax = 20
    ymin = 0
    ymax = 20

    @classmethod
    def in_bulk(cls, n, nrows=10):
        if n//nrows*nrows == n:
            a = n//nrows
            b = nrows
        else:
            a = n
            b = 1
        xs = np.linspace(cls.xmin, cls.xmax, a+1, endpoint=False)
        ys = np.linspace(cls.ymin, cls.ymax, b+1, endpoint=False)
        x, y = np.meshgrid(np.delete(xs, 0), np.delete(ys, 0))
        return [Particle([p[0], p[1]], [np.sin(2*np.pi*p[2]), np.cos(2*np.pi*p[2])])
                for p in zip(x.reshape(-1), y.reshape(-1), np.random.rand(n))
                ]

    def __init__(self, p = [0, 0], v = [1, 1]):
        self.p = np.array(p, dtype=float)
        self.v = np.array(v, dtype=float)

    def move(self, dt):
        # self.v = np.array([np.sin(phi), np.cos(phi)])
        newp = self.p + self.v.dot(dt)
        if newp[0] < self.xmin or newp[0] > self.xmax:
            self.v[0] *= -1
            newp[0] = self.p[0] + self.v[0]*dt
        if newp[1] < self.ymin or newp[1] > self.ymax:
            self.v[1] *= -1
            newp[1] = self.p[1] + self.v[1]*dt
        self.p = newp
        return self.p
    
    @property
    def x(self):
        return self.p[0]
    @property
    def y(self):
        return self.p[1]

    def __str__(self):
        return f"particle at {self.p} moving with speed {self.v}"


if __name__ == "__main__":
    p = Particle()
    p.move(0.1)
    print(p)
