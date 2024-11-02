import numpy as np
import ctypes
import math

# Load the shared library
# On Linux/macOS: math_operations.so
# On Windows: math_operations.dll
funcs = ctypes.CDLL('./funcs.so') 


# Define argument and return types for each function
funcs.add.argtypes = (ctypes.c_double, ctypes.c_double)
funcs.add.restype = ctypes.c_double

funcs.sub.argtypes = (ctypes.c_double, ctypes.c_double)
funcs.sub.restype = ctypes.c_double

funcs.mul.argtypes = (ctypes.c_double, ctypes.c_double)
funcs.mul.restype = ctypes.c_double

funcs.div.argtypes = (ctypes.c_double, ctypes.c_double)
funcs.div.restype = ctypes.c_double

funcs.sq_rt.argtypes = (ctypes.c_double,)
funcs.sq_rt.restype = ctypes.c_double

funcs.squar.argtypes = (ctypes.c_double,)
funcs.squar.restype = ctypes.c_double

# Define the coefficients for the quadratic equation y^2 + 6y - 27 = 0
a = 1.0
b = 6.0
c = -27.0

# Calculate discriminant
discriminant = funcs.sub(funcs.squar(b), funcs.mul(4, funcs.mul(a, c)))

# Calculate the two roots using the quadratic formula
sqrt_discriminant = funcs.sq_rt(discriminant)

if not math.isnan(sqrt_discriminant):
    root1 = funcs.div(funcs.sub(-b, sqrt_discriminant), funcs.mul(2, a))
    root2 = funcs.div(funcs.add(-b, sqrt_discriminant), funcs.mul(2, a))
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots.")

