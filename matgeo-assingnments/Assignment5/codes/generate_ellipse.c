#include <stdio.h>
#include <math.h>

#define A 4.0 // semi-major axis
#define B 3.0 // semi-minor axis
#define NUM_POINTS 100 // number of points to generate

int main() {
    FILE *file = fopen("ellipse_points.txt", "w"); // Open a file to save points
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate points on the ellipse
    for (int i = 0; i < NUM_POINTS; i++) {
        // Calculate the angle t
        double t = 2 * M_PI * i / NUM_POINTS;
        
        // Parametric equations for the ellipse
        double x = A * cos(t);
        double y = B * sin(t);
        
        // Write the points to the file
        fprintf(file, "%lf, %lf\n", x, y);
    }

    fclose(file); // Close the file
    printf("Generated %d points on the ellipse and saved to ellipse_points.txt\n", NUM_POINTS);
    return 0;
}

