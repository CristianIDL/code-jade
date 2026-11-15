import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

### We add the X, Y, Z axes
ax.plot([-1,1], [0,0], [0,0], color='r', label="PSI Interna")
ax.plot([0,0], [-1,1], [0,0], color='b', label="PSI Externa")
ax.plot([0,0], [0,0], [-1,1], color='g', label="PSI Inherente")

### We add some lil arrows for the axes
# quiver uses (x, y, z, u, v, w); 
    # x,y,z for the start; u,v,w for the direction
ax.quiver(0.8,0,0,0.2,0,0, color='r', arrow_length_ratio=0.5)
ax.quiver(0,0.8,0,0,0.2,0, color='b', arrow_length_ratio=0.5)
ax.quiver(0,0,0.8,0,0,0.2, color='g', arrow_length_ratio=0.5)


# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X-INTERNA/EXTERNA')
ax.set_ylabel('Y-MICRO/MACRO')
ax.set_zlabel('Z-INHERENTE/VIVA')

# We keep an aspect ratio of 1:1:1
ax.set_box_aspect((1, 1, 1))

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()