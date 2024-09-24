import numpy as np
import matplotlib.pyplot as plt

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
    
    # Direction vector (slope = 9/5)
    direction_vector = np.array([1, 9/5])
    
    # Normal vector (slope = -5/9)
    normal_vector = np.array([1, -5/9])

    # Length of the normal vector
    length = 10  # Arbitrary length for visualization

    # Normal vector end point
    c_norm_end = c_mid + length
    f_norm_end = f_mid + normal_vector[1] * (c_norm_end - c_mid)

    # Plot normal vector passing through the midpoint
    plt.quiver(c_mid, f_mid, c_norm_end - c_mid, f_norm_end - f_mid, 
               angles='xy', scale_units='xy', scale=1, color='red', label='Normal Vector')

    # Labels and title
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

