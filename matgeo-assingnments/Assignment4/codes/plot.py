import sys  # for path to external scripts
sys.path.insert(0, '/home/adishesh-balaji/github/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Function to read points from the txt file
def read_points_from_file(filename):
    c_values = []
    f_values = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by comma and convert to float
            c, f = map(float, line.strip().split(','))
            c_values.append(c)
            f_values.append(f)

    return np.array(c_values), np.array(f_values)

# Function to plot the line and its normal vector
def plot_line_and_normal(c_values, f_values):
    # Plot the line as a dotted line
    plt.plot(c_values, f_values, label=r'$F = \frac{9}{5}C + 32$', color='blue', linestyle='dotted')

    # Calculate the midpoint of the line
    midpoint_index = len(c_values) // 2
    c_mid = c_values[midpoint_index]
    f_mid = f_values[midpoint_index]

    # Midpoint as the starting point for the normal vector
    A_mid = np.array([c_mid, f_mid])

    # Direction vector (slope = 9/5)
    m = np.array([1, 9/5])

    # Normal vector (slope = -5/9)
    n = np.array([-9/5, 1])

    # Plot the main line using parametric form (starting at A = [0, 32])
    main_line_points = line_dir_pt(m, np.array([0, 32]), -50, 50)
    plt.plot(main_line_points[0, :], main_line_points[1, :], color='blue', linestyle='dotted')

    # Plot the normal vector emerging from the midpoint
    normal_points = line_dir_pt(n, A_mid, -20, 20)  # Adjust the range of the normal vector as needed
    plt.plot(normal_points[0, :], normal_points[1, :], label='Normal Vector', color='red', linestyle = 'dotted')

    # Set labels
    plt.xlabel('C (Celsius)')
    plt.ylabel('F (Fahrenheit)')
    plt.legend()

    # Set limits
    plt.xlim(-60, 110)
    plt.ylim(-70, 220)

    # Add grid
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Show the plot
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Main code execution
if __name__ == "__main__":
    filename = "line_points.txt"
    c_values, f_values = read_points_from_file(filename)
    plot_line_and_normal(c_values, f_values)

