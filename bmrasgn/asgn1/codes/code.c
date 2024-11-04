#include <stdio.h>
#include <stdlib.h>

// Function to generate points on the line F = (9/5)C + 32
void point_gen(FILE *fptr, double c1, double f1, double c2, double f2, int num_points) {
    for (int i = 0; i <= num_points; i++) {
        double t = (double)i / num_points;
        double c = c1 + t * (c2 - c1); // Linear interpolation for C
        double f = f1 + t * (f2 - f1); // Linear interpolation for F
        fprintf(fptr, "%lf,%lf\n", c, f);
    }
}

int main() {
    // Define two points on the line F = (9/5)C + 32
    double c1 = -50.0, f1 = (9.0 / 5.0) * c1 + 32.0;  // First point (C=-50, F)
    double c2 = 100.0, f2 = (9.0 / 5.0) * c2 + 32.0;  // Second point (C=100, F)
    
    // Open the file to save the points
    FILE *fptr = fopen("line_points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate points on the line
    point_gen(fptr, c1, f1, c2, f2, 63);  // Generate 63 points on the line

    // Normal vector generation
    // The slope of the line is 9/5, so the slope of the normal is -5/9.
    double c_normal = c1, f_normal = f1;  // Take the first point for normal vector
    double norm_slope = -5.0 / 9.0;       // Slope of the normal line
    double norm_length = 50.0;            // Arbitrary length for the normal line

    double c_norm_end = c_normal + norm_length;
    double f_norm_end = f_normal + norm_slope * (c_norm_end - c_normal);

    // Generate points on the normal line
    point_gen(fptr, c_normal, f_normal, c_norm_end, f_norm_end, 20);

    // Close the file
    fclose(fptr);

    printf("Points on the line and normal vector saved to line_points.txt\n");

    return 0;
}

