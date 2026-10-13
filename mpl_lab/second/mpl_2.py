import matplotlib.pyplot as plt
import math

filename = 'data.dat'

with open(filename, encoding='utf-8') as f:
    lines = [list(map(float, l.split())) for l in f if l.strip()]

frames = list(zip(lines[::2], lines[1::2]))
xs_all = [x for xs, _ in frames for x in xs]
ys_all = [y for _, ys in frames for y in ys]

fig, axes = plt.subplots(math.ceil(len(frames)/2), 2,
                         figsize=(12, 3 * math.ceil(len(frames)/2)))
axes = axes.flatten()

for i, (xs, ys) in enumerate(frames):
    axes[i].plot(xs, ys)
    axes[i].set(title=f'Frame {i}',
                xlim=(min(xs_all), max(xs_all)),
                ylim=(min(ys_all), max(ys_all)),
                aspect='equal')
    axes[i].grid(True, which='both')
    axes[i].minorticks_on()

for ax in axes[len(frames):]:
    ax.axis('off')

plt.tight_layout()
plt.savefig('frames.png', dpi=150, bbox_inches='tight')
plt.show()