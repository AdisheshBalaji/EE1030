#include <stdio.h>
#include <math.h>

int main() {
    double x1 = 10.0, y1 = -9.0;
    double x2 = 2.0, y2 = -3.0;
    double x3 = 10.0, y3 = 3.0;
    
    double distance1 = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    double distance2 = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2));
   FILE *file = fopen("output.txt", "w");

    if (file == NULL) {
        fprintf(stderr, "Error opening file!\n");
        return 1;
    }

    fprintf(file, "The distance between the points (%.1f, %.1f) and (%.1f, %.1f) is %.2f\n", x1, y1, x2, y2, distance1);
    fprintf(file, "The distance between the points (%.1f, %.1f) and (%.1f, %.1f) is %.2f\n", x2, y2, x3, y3, distance2);

    fclose(file);
return 0;
}
