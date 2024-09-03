import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
with open("data.txt", 'r') as f:
    L = f.readlines()
a = []
for line in L:
    row = line.strip().split()  
    row = [int(x) for x in row]  
    a.append(row)
A=a[0]
B=a[1]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], label=['A', 'B'])
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]])
ax.text(*A, f'A({A[0]}, {A[1]}, {A[2]})')
ax.text(*B, f'B({B[0]}, {B[1]}, {B[2]})')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
