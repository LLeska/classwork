import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.animation import FuncAnimation

mode = 0
while mode not in range(1, 4):
    try:
        mode = int(input("Choose task\n 1 - Lunar images\n 2 - Signals\n 3 - Dynamics\n"))
        if mode not in range(1, 4):
            print("incorrect number, try again")
    except ValueError:
        print("incorrect number, try again")

if mode == 1:
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(9, 10))
    for i in range(1, 4):
        img = Image.open(f"data/lunar_images/lunar0{i}_raw.jpg")
        data = np.array(img, dtype=float)
        new_data = (data - data.min()) * 255 / (data.max() - data.min())
        new_data = new_data.astype(np.uint8)
        Image.fromarray(new_data).save(f"data/lunar_images/lunar0{i}_processed.png")

        axs[i - 1][0].imshow(data, cmap="gray", vmin=0, vmax=255)
        axs[i - 1][1].imshow(new_data, cmap="gray", vmin=0, vmax=255)
        axs[i - 1][0].set_title(f"Image {i} - before")
        axs[i - 1][1].set_title(f"Image {i} - after")
        axs[i - 1][0].axis("off")
        axs[i - 1][1].axis("off")
    plt.tight_layout()
    plt.show()

elif mode == 2:
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10, 9))
    for i in range(1, 4):
        data = np.loadtxt(f"data/signals/signal0{i}.dat")
        filtered = np.zeros(len(data))
        for j in range(len(data)):
            filtered[j] = np.mean(data[max(0, j - 9):j + 1])

        axs[i - 1][0].plot(data)
        axs[i - 1][1].plot(filtered)
        axs[i - 1][0].set_title(f"Signal {i} - before")
        axs[i - 1][1].set_title(f"Signal {i} - after")
        axs[i - 1][0].grid(True)
        axs[i - 1][1].grid(True)
    plt.tight_layout()
    plt.show()

elif mode == 3:
    data = np.loadtxt("data/start.dat.txt")
    if data.ndim == 1:
        x = np.arange(len(data))
        u = data
    else:
        x = data[:, 0]
        u = data[:, 1]

    steps = [u.copy()]
    for i in range(255):
        u = 0.5 * (u + np.roll(u, 1))
        steps.append(u.copy())

    fig, ax = plt.subplots(figsize=(8, 5))
    line, = ax.plot(x, steps[0])
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(0, max(steps[0]) * 1.1)
    ax.grid(True)

    def update(i):
        line.set_ydata(steps[i])
        ax.set_title(f"Step {i}")
        return line,

    animation = FuncAnimation(fig, update, frames=len(steps), interval=80)
    plt.show()