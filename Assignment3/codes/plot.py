import sys                                  
sys.path.insert(0, '/home/matgeo/codes/CoordGeo/line')    
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from funcs import line_gen
import params

A = np.array(([10 , -9]))
B = np.array(([2, -3]))
C = np.array(([10, 3]))

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

plt.figure(figsize=(8, 6))

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')


plt.text(A[0], A[1], 'A(10,-9)')
plt.text(B[0], B[1], 'B(2,-3)')
plt.text(C[0], C[1], 'C(10,3)')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Plot of the two possible points A and C which are 5 units away from B')
plt.legend()
plt.grid(True)


plt.savefig('plot.png')
