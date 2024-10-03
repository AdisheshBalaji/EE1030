import subprocess
import numpy as np
import matplotlib.pyplot as plt


# Step 3: Load points from the generated file
points = np.loadtxt('ellipse_points.txt', delimiter=',')  # Load x and y points

# Step 4: Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Step 5: Plot the ellipse
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Ellipse', color='blue')
plt.fill(x, y, color='lightblue', alpha=0.3)  # Fill the ellipse with color
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # X-axis
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')  # Y-axis
plt.xlim(-5, 5)  # Set limits for x-axis
plt.ylim(-4, 4)  # Set limits for y-axis
plt.gca().set_aspect('equal', adjustable='box')  # Set equal scaling
plt.grid(True)
plt.legend()
plt.show()

