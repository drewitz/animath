from modules.population import Population
from modules.data_write import write_data

tmax = 10

meta_data = {
    "title": "SIR Model",
    "timestamps": [0, tmax],
    "filename": "sir-model.mp4",
    "path": "videos/"
}


pop = Population(4*3600, nrows=60*2)
dest = pop.animate(tmax=tmax, dt=0.1)
#pop.show()
write_data(meta_data)
dest.save("docs/videos/sir-model.mp4")
