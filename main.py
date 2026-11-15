import matplotlib.pyplot as plt
from psyconfig import *

ax = plt.figure().add_subplot(projection='3d')

### We add the X, Y, Z axes
ax.plot([-1,1], [0,0], [0,0], color='b', label="Psique")
ax.plot([0,0], [-1,1], [0,0], color='r', label="Nivel")
ax.plot([0,0], [0,0], [-1,1], color='g', label="Materia")

### We add some lil arrows for the axes
# quiver uses (x, y, z, u, v, w); 
    # x,y,z for the start; u,v,w for the direction
ax.quiver(0.8,0,0,0.2,0,0, color='b', arrow_length_ratio=0.5)
ax.quiver(0,0.8,0,0,0.2,0, color='r', arrow_length_ratio=0.5)
ax.quiver(0,0,0.8,0,0,0.2, color='g', arrow_length_ratio=0.5)

### We add the scatter points for each class
xs = [point["coords"][0] for point in CLASSES]
ys = [point["coords"][1] for point in CLASSES]
zs = [point["coords"][2] for point in CLASSES]
colors = [point["color"] for point in CLASSES]
sizes = [point["size"] for point in CLASSES]

# Plot the scatter points
ax.scatter(
    xs, ys, zs,
    c=colors,
    s=sizes,
)

for point in CLASSES:
    x, y, z = point["coords"]
    ax.text(x, y, z, point["name"], fontsize=10)

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('INTERNA -> EXTERNA')
ax.set_ylabel('MICRO -> MACRO')
ax.set_zlabel('INHERENTE -> VIVA')

# We keep an aspect ratio of 1:1:1
ax.set_box_aspect((1, 1, 1))

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()