import sys                                  
sys.path.insert(0, '/home/github/matgeo/codes/CoordGeo/line')    
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the function to generate lines between two points
def line_gen(A, B):
    len = 100  # Number of points in the line
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam = np.linspace(0, 1, len)
    for i in range(len):
        x_AB[:, i] = A + lam[i] * (B - A)
    return x_AB

# Define points
Q1 = np.array(([10 , -9]))
P = np.array(([2, -3]))
Q2 = np.array(([10, 3]))

# Generate lines
x_PQ1 = line_gen(P, Q1)
x_PQ2 = line_gen(P, Q2)

# Plot the figure
plt.figure(figsize=(8, 6))

plt.plot(x_PQ1[0,:], x_PQ1[1,:], label='$PQ1$')
plt.plot(x_PQ2[0,:], x_PQ2[1,:], label='$PQ2$')

# Label the points
plt.text(Q1[0], Q1[1], 'Q1(10,-9)')
plt.text(P[0], P[1], 'P(2,-3)')
plt.text(Q2[0], Q2[1], 'Q2(10,3)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('plot.png')

