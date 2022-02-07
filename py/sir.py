from modules.population import Population

pop = Population(3600, nrows=60)
dest = pop.animate(tmax=6, dt=0.1)
pop.show()
#dest.save("docs/videos/sir-model.mp4")