import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


tmax = 100

meta_data = {
    "title": "SIR Model 2",
    "timestamps": [0, tmax],
    "filename": "sir-model2.mp4",
    "path": "videos/"
}

# s' = -a*s*i
# i' = a*s*i - b*i
# r' = b*i

a = 0.5
b = 0.1

def model(vec, t):
    """ vec = [s, i, r]
    """
    return [-a*vec[0]*vec[1], a*vec[0]*vec[1] - b*vec[1], b*vec[1]]

t = np.linspace(0, tmax, 100)

sol = odeint(model, [0.9, 0.1, 0], t)

plt.plot(t, sol)
plt.show()

print(f"docs/{meta_data['path']}{meta_data['filename']}")
