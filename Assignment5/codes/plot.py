import numpy as np
import matplotlib.pyplot as plt

# Step 3: Load points from the generated file
points = np.loadtxt('ellipse_points.txt', delimiter=',')  # Load x and y points

# Step 4: Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Step 5: Plot the ellipse
plt.figure(figsize=(8, 6))

# Ellipse parameters
a = 4  # semi-major axis
b = 3  # semi-minor axis
center_x = 0
center_y = 0
vertices = [(0, -3), (0, 3)]  # Minor axis points
covertices = [(4, 0), (-4, 0)]  # Major axis points
center = (0, 0)

# Plot the ellipse
plt.plot(x, y, label='Ellipse', color='blue')

# Plot and label the vertices
plt.scatter(*zip(*vertices), color="red", label="Vertices")
for vx, vy in vertices:
    plt.text(vx + 0.1, vy + 0.1, f'({vx}, {vy})', fontsize=10, color='red')

# Plot and label the covertices
plt.scatter(*zip(*covertices), color="green", label="Covertices")
for cvx, cvy in covertices:
    plt.text(cvx + 0.1, cvy + 0.1, f'({cvx}, {cvy})', fontsize=10, color='green')

# Plot and label the center
plt.scatter(center[0], center[1], color="yellow", label="Center")
plt.text(center[0] + 0.1, center[1] + 0.1, f'({center[0]}, {center[1]})', fontsize=10, color='yellow')

# Fill the ellipse with color
plt.fill(x, y, color='lightblue', alpha=0.3)

# Set up plot labels and appearance
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # X-axis
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')  # Y-axis
plt.xlim(-5, 5)  # Set limits for x-axis
plt.ylim(-4, 4)  # Set limits for y-axis
plt.gca().set_aspect('equal', adjustable='box')  # Set equal scaling
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

