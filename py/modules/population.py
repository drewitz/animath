"""Population module

implements a population of particles
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from modules.particle import Particle


col_s = "#0777ba"
col_i = "#ee003c"
col_r = "#5be800"

class Population:
    """Population is a collection of particles
    """

    recover_time = 5
    # diameter of particles
    diameter = 0.2
    # setup plot
    background = "black"


    def __init__(self, psize=100, nrows=10, ninfected=5, bdies=None, speed=1, rec_time=2.5):
        self.recover_time = rec_time
        if bdies is not None:
            Particle.set_bdy(*bdies)
        self.psize = psize
        # create particles on a line at first
        self.pop = Particle.in_bulk(psize, nrows, speed=speed)
        # save indices of susceptible, infected and recovered
        self.infected = np.random.choice(np.arange(psize), ninfected)
        self.susceptible = np.setdiff1d(np.arange(psize), self.infected)
        self.recovered = np.array([], dtype=int)
        self.inftime = np.ones(psize)*self.recover_time
        for i in self.recovered:
            self.inftime[i] = 0


    def calculate(self, tmax, dt):
        t = 0
        self.data = {
            "xs": [np.array([p.x for p in self.pop])],
            "ys": [np.array([p.y for p in self.pop])],
            "inf": [self.infected],
            "sus": [self.susceptible],
            "rec": [self.recovered],
            "n" : 1,
            "ninf": [len(self.infected)],
            "nsus": [len(self.susceptible)],
            "nrec": [len(self.recovered)]
            }
        while t < tmax:
            t += dt
            newxs = np.array([])
            newys = np.array([])
            for p in self.pop:
                p.move(dt)
                newxs = np.append(newxs, p.x)
                newys = np.append(newys, p.y)
            self.data["xs"].append(newxs)
            self.data["ys"].append(newys)
            self.data["n"] += 1
            meets = self.check_meeting(newxs, newys)
            if meets[0].size > 0:
                for i in range(meets[0].size):
                    self.collide(meets[0][i], meets[1][i])
            # recover:
            for i in self.infected:
                self.inftime[i] -= dt
                if self.inftime[i] <= 0:
                    # recover
                    self.inftime[i] = 0
                    self.recovered = np.append(self.recovered, i)
                    self.infected = self.infected[np.where(self.infected!=i)]
            self.data["inf"].append(self.infected)
            self.data["sus"].append(self.susceptible)
            self.data["rec"].append(self.recovered)

            self.data["ninf"].append(len(self.infected))
            self.data["nsus"].append(len(self.susceptible))
            self.data["nrec"].append(len(self.recovered))
            
        return self.data

    def check_meeting(self, xs, ys):
        xa, xb = np.meshgrid(xs, xs)
        ya, yb = np.meshgrid(ys, ys)
        # get indices where distance is smaller than diameter
        xi, yi = np.where(np.square(xa - xb) + np.square(ya - yb) < self.diameter**2)
        # only want the ones where the first index is smaller than the second
        # - if both indices are the same, then distance is 0
        # - there are two occurences of these pairs
        result = np.where(xi < yi)
        return (xi[result], yi[result])

    def collide(self, i, j):
        tempv = self.pop[i].v
        self.pop[i].v = self.pop[j].v
        self.pop[j].v = tempv
        # check for infection
        if i in self.infected:
            if j in self.susceptible:
                self.infected = np.append(self.infected, j)
                self.susceptible = self.susceptible[np.where(self.susceptible!=j)]
        elif i in self.susceptible:
            if j in self.infected:
                self.infected = np.append(self.infected, i)
                self.susceptible = self.susceptible[np.where(self.susceptible!=i)]


    @property
    def positions(self):
        return [p.p for p in self.pop]
    
    def next_step(self, i):
        # infected
        xinf = self.data["xs"][i][self.data["inf"][i]]
        yinf = self.data["ys"][i][self.data["inf"][i]]
        self.dotsinf.set_data(xinf, yinf)
        # susceptible
        xsus = self.data["xs"][i][self.data["sus"][i]]
        ysus = self.data["ys"][i][self.data["sus"][i]]
        self.dotssus.set_data(xsus, ysus)
        # susceptible
        xrec = self.data["xs"][i][self.data["rec"][i]]
        yrec = self.data["ys"][i][self.data["rec"][i]]
        self.dotsrec.set_data(xrec, yrec)
        # graphs
        self.pinf.set_data(self.t[:i+1], self.data["ninf"][:i+1])
        self.psus.set_data(self.t[:i+1], self.data["nsus"][:i+1])
        self.prec.set_data(self.t[:i+1], self.data["nrec"][:i+1])
        return self.dotsinf, self.dotssus, self.dotsrec, self.pinf, self.psus, self.prec

    def animate(self, tmax=1, dt=0.1):
        data = self.calculate(tmax, dt)
        self.tmax = tmax
        self.dt = dt

        # setup plot
        fig, axes = plt.subplots(1,2, figsize=(16, 9))
        fig.patch.set_facecolor(self.background)
        ax = axes[0]
        ax.set_xlim(Particle.xmin, Particle.xmax)
        ax.set_ylim(Particle.ymin, Particle.ymax)
        ax.set_axis_off()
        
        # plot graphs
        ax2 = axes[1]
        ax2.set_xlim(0, tmax)
        ax2.set_ylim(0, self.psize)
        self.t = np.linspace(0, tmax, data["n"])
        self.pinf, = ax2.plot(self.t[:1], data["ninf"][:1], col_i)
        self.psus, = ax2.plot(self.t[:1], data["nsus"][:1], col_s)
        self.prec, = ax2.plot(self.t[:1], data["nrec"][:1], col_r)

        # infected
        xinf = data["xs"][0][data["inf"][0]]
        yinf = data["ys"][0][data["inf"][0]]
        self.dotsinf, = ax.plot(xinf, yinf, "o", color=col_i, markersize=5)
        # susceptible
        xsus = data["xs"][0][data["sus"][0]]
        ysus = data["ys"][0][data["sus"][0]]
        self.dotssus, = ax.plot(xsus, ysus, "o", color=col_s, markersize=5)
        # susceptible
        xrec = data["xs"][0][data["rec"][0]]
        yrec = data["ys"][0][data["rec"][0]]
        self.dotsrec, = ax.plot(xrec, yrec, "o", color=col_r, markersize=5)

        self.anim = animation.FuncAnimation(fig, self.next_step, frames=data["n"], interval=dt*1000)
        return self.anim
        
    def show(self):
        plt.show()
    
    def save(self, dest="sir-animation.mp4"):
        mw = animation.FFMpegWriter()
        self.anim.save(dest, writer=mw)


if __name__ == "__main__":
    pop = Population(4*3600, nrows=60*2)
    dest = pop.animate(tmax=6, dt=0.1)
    dest.show()
