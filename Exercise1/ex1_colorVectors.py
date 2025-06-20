import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the vectors
v1 = np.array([40, 120, 60])
v2 = np.array([60, 50, 90])

# Create a 3D plot
fig = plt.figure().add_subplot(projection='3d')

# Plot the vectors as points (endpoints)
fig.scatter(v1[0], v1[1], v1[2], s=100, color='blue', label='Vector 1 (40,120,60)')
fig.scatter(v2[0], v2[1], v2[2], s=100, color='red', label='Vector 2 (60,50,90)')

# Plot the origin
fig.scatter(0, 0, 0, s=100, color='black', label='Origin')

# Draw arrows from the origin to the vectors
# ax.quiver(x_origin, y_origin, z_origin, x_component, y_component, z_component, ...)
fig.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue', arrow_length_ratio=0.08)
fig.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='red', arrow_length_ratio=0.08)


# Set labels and limits
fig.set_xlabel('X')
fig.set_ylabel('Y')
fig.set_zlabel('Z')
fig.set_xlim(0, 150)
fig.set_ylim(0, 150)
fig.set_zlim(0, 150)

# Customize the view angle for better visualization
fig.view_init(elev=20., azim=-35, roll=-10)

# Add a legend
fig.legend()

# Show the plot
plt.title('3D Vector Visualization')
plt.show()