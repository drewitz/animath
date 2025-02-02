from modules.population import Population

from numpy.random import seed
seed(31415)

tmax = 25

pop = Population(4*3600, nrows=2*60, bdies=[0, 40, 0, 40], speed=0.8)
dest = pop.animate(tmax=tmax, dt=0.1)
#pop.show()
dest.save("docs/videos/sir-model.mp4")

pop = Population(100, nrows=10, bdies=[0, 7, 0, 7], speed=0.5)
dest = pop.animate(tmax=tmax, dt=0.1)
#pop.show()
dest.save("docs/videos/sir-model-klein.mp4")
