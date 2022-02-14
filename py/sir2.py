import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import odeint

tmax = 25

meta_data = {
    "title": "SIR Model 2",
    "timestamps": [0, tmax],
    "filename": "sir-model2.mp4",
    "path": "videos/"
}

# s' = -a*s*i
# i' = a*s*i - b*i
# r' = b*i
col_s = "#0777ba"
col_i = "#ee003c"
col_r = "#5be800"


# diff eqn Parameter
a = 0.5
b = 0.05

# start parameter
s0 = 0.99
i0 = 1-s0
r0 = 0

def model(vec, t, a=a, b=b):
    """ vec = [s, i, r]
    """
    return [-a*vec[0]*vec[1], a*vec[0]*vec[1] - b*vec[1], b*vec[1]]

t = np.linspace(0, tmax, 100)

sol = odeint(model, [s0, i0, r0], t)

fig, ax1 = plt.subplots(1, 1)
#axs[0].bar([1, 2, 3], sol[20], color=[col_s, col_i, col_r])]
lines = []
for i, c in enumerate(zip([col_s, col_i, col_r], ["Susceptible", "Infectuous", "Recovered"])):
    lines += ax1.plot(t, sol[:,i], color=c[0], label=c[1])
plt.legend()


plt.subplots_adjust(bottom=0.4)
# Make a horizontal slider to control the frequency.
ax_slide = plt.axes([0.25, 0.1, 0.65, 0.03])
slide_a = Slider(
    ax=ax_slide,
    label='parameter a',
    valmin=0,
    valmax=2,
    valinit=a,
)

ax_slide = plt.axes([0.25, 0.25, 0.65, 0.03])
slide_b = Slider(
    ax=ax_slide,
    label='parameter b',
    valmin=0,
    valmax=2,
    valinit=b,
)

def update(val):
    sol = odeint(model, [s0, i0, r0], t, args=(slide_a.val, slide_b.val))
    for i in range(3):
        lines[i].set_ydata(sol[:, i])
    fig.canvas.draw_idle()

slide_a.on_changed(update)
slide_b.on_changed(update)

plt.show()

print(f"docs/{meta_data['path']}{meta_data['filename']}")
