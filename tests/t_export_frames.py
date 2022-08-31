from pathlib import Path
from anim.generate_imgs import export_frames, movie
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import tempfile

fig, ax = plt.subplots()
line, = ax.plot([], [])

def init():
    x = np.linspace(0, 2*np.pi)
    y = np.sin(x)
    line.set_data(x,y)

def update(frame):
    x = np.linspace(0, 2*np.pi)
    y = np.sin(x - frame)
    line.set_data(x, y) 

frames = np.linspace(0,1)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
anim = FuncAnimation(fig, update, frames, init_func=init, interval = 1000/60)


plt.show()

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

    export_frames(anim, tmpdirname, len(frames))

    files = [x for x in Path(tmpdirname).glob("**/*") if x.is_file()]

    print(files)


movie(anim, "movie.mp4", len(frames), 60)
