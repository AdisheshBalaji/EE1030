import sys                                  
sys.path.insert(0, '/home/matgeo/codes/CoordGeo/line')    
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from funcs import line_gen
import params

B1 = np.array(([10 , -9]))
A = np.array(([2, -3]))
B2 = np.array(([10, 3]))

x_AB1 = line_gen(A,B1)
x_AB2 = line_gen(A,B2)

plt.figure(figsize=(8, 6))

plt.plot(x_AB1[0,:],x_AB1[1,:],label='$AB1$')
plt.plot(x_AB2[0,:],x_AB2[1,:],label='$AB2$')


plt.text(B1[0], B1[1], 'B1(10,-9)')
plt.text(A[0], A[1], 'A(2,-3)')
plt.text(B2[0], B2[1], 'B(10,3)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of the two possible points B1 and B2 which are 10 units away from A')
plt.legend()
plt.grid(True)


plt.savefig('plot.png')
