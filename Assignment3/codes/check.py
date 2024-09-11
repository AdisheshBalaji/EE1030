import ctypes
import math

# Load the shared library
# On Linux/macOS: math_operations.so
# On Windows: math_operations.dll
lib = ctypes.CDLL('add.so') 
lib = ctypes.CDLL('sub.so')
lib = ctypes.CDLL('mul.so')
lib = ctypes.CDLL('sq_rt.so')
lib = ctypes.CDLL('squar.so')
lib = ctypes.CDLL('div.so')

# Define argument and return types for each function
lib.add.argtypes = (ctypes.c_double, ctypes.c_double)
lib.add.restype = ctypes.c_double

lib.sub.argtypes = (ctypes.c_double, ctypes.c_double)
lib.sub.restype = ctypes.c_double

lib.mul.argtypes = (ctypes.c_double, ctypes.c_double)
lib.mul.restype = ctypes.c_double

lib.div.argtypes = (ctypes.c_double, ctypes.c_double)
lib.div.restype = ctypes.c_double

lib.sq_rt.argtypes = (ctypes.c_double,)
lib.sq_rt.restype = ctypes.c_double

lib.squar.argtypes = (ctypes.c_double,)
lib.squar.restype = ctypes.c_double

# Define the coefficients for the quadratic equation y^2 + 6y - 27 = 0
a = 1.0
b = 6.0
c = -27.0

# Calculate discriminant
discriminant = lib.sub(lib.squar(b), lib.mul(4, lib.mul(a, c)))

# Calculate the two roots using the quadratic formula
sqrt_discriminant = lib.sq_rt(discriminant)

if not math.isnan(sqrt_discriminant):
    root1 = lib.div(lib.sub(-b, sqrt_discriminant), lib.mul(2, a))
    root2 = lib.divide(lib.add(-b, sqrt_discriminant), lib.mul(2, a))
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots.")

