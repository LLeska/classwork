import matplotlib.pyplot as plt
flag = True
mode = 0
while flag or mode not in range(1,4):
    try:
        mode = input("Choose task \n 1 - Dead moroz \n 2 - Frames \n 3 - Students \n")
        mode = int(mode)
        flag = False
    except ValueError:
        print("incorrect number, try again")
flag = True
if mode == 1:
    choose = "0"
    while flag and choose not in "12345":
        choose = input("Choose file (1-5)\n")
        try:
            with open(f"dead_moroz/00{choose}.dat", "r") as file:
                n = int(file.readline())
                x = []
                y = []
                for _ in range(n):
                    xi, yi = map(float, file.readline().split())
                    x.append(xi)
                    y.append(yi)
                width = max(x) - min(x)
                height = max(y) - min(y)
                max_width = 12
                max_height = 7
                scale = min(max_width / max(width, 1), max_height / max(height, 1))
                fig_width = max(3, width * scale)
                fig_height = max(3, height * scale)
                fig = plt.figure(figsize=[fig_width, fig_height])
                plt.scatter(x, y)
                plt.title(f"Number of points: {len(x)}")
                plt.show()
                file.close()
        except FileNotFoundError:
            print("incorrect number, try again")
elif mode == 2:
    with open(f"frames.dat", "r") as file:
        flag = False
        lines = file.readlines()
        x = []
        y = []
        for i in range(0, len(lines), 2):
            x.append(list(map(float, lines[i].split())))
            y.append(list(map(float, lines[i + 1].split())))
        fig, axs = plt.subplots(nrows=3, ncols=2,figsize=(7, 10), sharex=True, sharey=True)
        for i in range(len(x)):
            axs[i // 2][i % 2].plot(x[i], y[i])
            axs[i // 2][i % 2].set_title(f"Frame {i}")
            axs[i // 2][i % 2].grid(True)
            axs[i // 2][i % 2].set_xlim(0, 16)
            axs[i // 2][i % 2].set_ylim(-9, 12)
            axs[i // 2][i % 2].set_xticks(range(0, 17, 2))
            axs[i // 2][i % 2].set_yticks(range(-8, 13, 2))
            axs[i // 2][i % 2].tick_params(labelbottom=True, labelleft=True)
            axs[i // 2][i % 2].set_box_aspect(1)
        plt.subplots_adjust(hspace=0.5)
        plt.show()
        file.close()
elif mode == 3:
    preps = {}
    groups = {}
    with open("students.csv", "r") as file:
        for line in file:
            prep, group, mark = line.split(";")
            mark = int(mark)
            if prep not in preps:
                preps[prep] = [0] * 11
            if group not in groups:
                groups[group] = [0] * 11
            preps[prep][mark] += 1
            groups[group][mark] += 1
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
    for i in range(2):
        if i == 0:
            data = preps
            title = "Marks per prep"
        else:
            data = groups
            title = "Marks per group"
        names = sorted(data)
        bottom = [0] * len(names)
        for mark in range(1, 11):
            values = []
            for name in names:
                values.append(data[name][mark])
            axs[i].bar(names, values, bottom=bottom, label=str(mark))
            for j in range(len(names)):
                bottom[j] += values[j]
        axs[i].set_title(title)
        handles, labels = axs[i].get_legend_handles_labels()
        axs[i].legend(handles[::-1], labels[::-1])
    plt.subplots_adjust(hspace=0.35)
    plt.show()
    file.close()