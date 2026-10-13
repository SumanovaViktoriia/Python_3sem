import matplotlib.pyplot as plt


files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']


fig, axes = plt.subplots(1, 5, figsize=(25, 5))

for ax, filename in zip(axes, files):
    try:
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            
            xs, ys = [], []
            for _ in range(n):
                x, y = map(float, f.readline().split())
                xs.append(x)
                ys.append(y)
        
        ax.scatter(xs, ys, s=10, alpha=0.7)
        ax.set_title(f'Number of points: {n}')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
    
    except FileNotFoundError:
        ax.set_title(f'{filename}: not found')
        ax.axis('off')

plt.tight_layout()
plt.savefig('visualization.png', dpi=100)
plt.show()