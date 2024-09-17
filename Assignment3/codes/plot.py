import sys                                  
sys.path.insert(0, '/home/matgeo/codes/CoordGeo/line')    
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from funcs import line_gen
import params

Q1 = np.array(([10 , -9]))
P = np.array(([2, -3]))
Q2 = np.array(([10, 3]))

x_PQ1 = line_gen(P,Q1)
x_PQ2 = line_gen(P,Q2)

plt.figure(figsize=(8, 6))

plt.plot(x_PQ1[0,:],x_PQ1[1,:],label='$PQ1$')
plt.plot(x_PQ2[0,:],x_PQ2[1,:],label='$PQ2$')


plt.text(Q1[0], Q1[1], 'Q1(10,-9)')
plt.text(P[0], P[1], 'P(2,-3)')
plt.text(Q2[0], Q2[1], 'Q2(10,3)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')www
plt.title('Plot of the two possible points Q1 and Q2 which are 10 units away from P')
plt.legend()
plt.grid(True)


plt.savefig('plot.png')
