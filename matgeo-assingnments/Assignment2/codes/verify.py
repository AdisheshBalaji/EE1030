import numpy as np
import ctypes
func=ctypes.CDLL('/home/adishesh-balaji/EE1030/Assignment2/codes/add.so')

A=[2,-3,4]
B=[-4,6,-8]
C=[0,0,0]

if func.add(B[0],2*A[0])==C[0] and func.add(B[1],2*A[1])==C[1] and func.add(B[2],2*A[2])==C[2] :
    print("Rank 1 and thus A,B,C collinear")
else:
    print("A,B,C not collinear")
