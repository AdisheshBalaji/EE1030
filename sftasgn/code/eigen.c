
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

#define EPSILON 1e-9
#define MAX_ITER 5000
// householder reflections for QR decomposn
void qr_decomposition(double complex** A, int n, double complex** Q, double complex** R) {
    // set R as a copy of A initially
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            R[i][j] = A[i][j];
        }
    }

    // Initialize Q as I
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
           if(i==j){
            Q[i][j] = 1.0 + 0.0*I;
           }else{
            Q[i][j] = 0.0 + 0.0*I;
           }
        }
    }

    for (int k = 0; k < n - 1; k++) {
        // calculate the norm for elements below a_ii for H_i
        double norm = 0.0;
        for (int i=k;i<n;i++) {
            norm += creal(R[i][k])*creal(R[i][k]) + cimag(R[i][k])*cimag(R[i][k]);
        }
        norm = sqrt(norm);

        // form the Householder vector
        double complex* v = (double complex*)calloc(n, sizeof(double complex));
        for (int i=0;i<n;i++) {
            if(i<k){
                v[i] = 0.0 + 0.0*I;
            }else{
                v[i] = R[i][k];
            }
        }
        v[k] += (creal(R[k][k]) > 0 ? norm : -norm);
        // normalize v
        double v_norm = 0.0;
        for (int i=k;i<n;i++) {
            v_norm += creal(v[i])*creal(v[i]) + cimag(v[i])*cimag(v[i]);
        }
        v_norm = sqrt(v_norm);
        for (int i=0;i<n;i++) {
            v[i] = v[i]/v_norm;
        }

        // calculate the householder transformn: H = I - 2*v*v^H
        double complex** H = (double complex**)malloc(n * sizeof(double complex*));
        for (int i=0;i<n;i++) {
            H[i] = (double complex*)malloc(n * sizeof(double complex));
            for (int j=0;j<n;j++) {
               
                if(i==j){
                    H[i][j] = 1.0 + 0.0*I - 2.0*v[i]*conj(v[j]);
                }else{
                    H[i][j] = -2.0*v[i]*conj(v[j]);
                }
            }
        }

        // update R as H*R
        double complex** temp = (double complex**)malloc(n * sizeof(double complex*));
        for (int i=0;i<n;i++) {
            temp[i] = (double complex*)calloc(n, sizeof(double complex)); //use temp for update
            for (int j=0;j<n;j++) {
                for (int p = 0; p < n; p++) {
                    temp[i][j] += H[i][p] * R[p][j];
                }
            }
        }
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                R[i][j] = temp[i][j]; //copy and then free the temp
            }
        }

        
        // update Q by multipying by H^H
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                temp[i][j] = 0.0 + 0.0 * I;
                for (int p = 0; p < n; p++) {
                    temp[i][j] += Q[i][p] * conj(H[j][p]);
                }
            }
        }
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                Q[i][j] = temp[i][j];
            }
        }

        // free memory
        for (int i=0;i<n;i++) {
            free(H[i]);
            free(temp[i]);
        }
        free(H);
        free(temp);
        free(v);
    }
}

// function for iterative qr algo
void qr_algorithm(double complex** A, int n, double complex* eigenvalues) {
    double complex** Q = (double complex**)malloc(n * sizeof(double complex*));
    double complex** R = (double complex**)malloc(n * sizeof(double complex*));
    for (int i=0;i<n;i++) {
        Q[i] = (double complex*)malloc(n * sizeof(double complex));
        R[i] = (double complex*)malloc(n * sizeof(double complex));
    }

    // decomposing A_k into QR
    for (int iter = 0; iter < MAX_ITER; iter++) {
        qr_decomposition(A, n, Q, R);

        //updating A_k+1
        double complex** newA = (double complex**)malloc(n * sizeof(double complex*));
        for (int i=0;i<n;i++) {
            newA[i] = (double complex*)calloc(n, sizeof(double complex));
            for (int j=0;j<n;j++) {
                for (int k = 0; k < n; k++) {
                    newA[i][j] += R[i][k] * Q[k][j];
                }
            }
        }

        // check convergence
        int converged = 1;
        for (int i = 0; i < n - 1; i++) {
            if (cabs(newA[i + 1][i]) > EPSILON) {
                converged = 0; //not converged
                break;
            }
        }
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                printf("%lf + %lfi", creal(newA[i][j]), cimag(newA[i][j]));
            }
        }*/
        for (int i=0;i<n;i++) {
            free(A[i]);
            A[i] = newA[i];
        }
        free(newA);

        if (converged) {
            break; //return to print eigen values
        }
    }

    // extract the diagonal elements
    for (int i=0;i<n;i++) {
        eigenvalues[i] = A[i][i];
    }

    // free memory
    for (int i=0;i<n;i++) {
        free(Q[i]); //freeing double pointers
        free(R[i]);
    }
    free(Q);
    free(R);
}

int main() {
    int n;
    printf("Enter the size of the matrix: ");
    scanf("%d", &n);

    double complex** A = (double complex**)malloc(n * sizeof(double complex*));
    for (int i=0;i<n;i++) {
        A[i] = (double complex*)malloc(n * sizeof(double complex));
    }

    printf("Enter the elements of the matrix:\n");
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            double real, imag;
            scanf("%lf %lf", &real, &imag);
            A[i][j] = real + imag*I;
        }
    }

    double complex* eigenvalues = (double complex*)malloc(n * sizeof(double complex));

    // Perform the QR algorithm
    qr_algorithm(A, n, eigenvalues);

    printf("Eigenvalues of the matrix are:\n");
    for (int i=0;i<n;i++) {
        printf("%lf + %lfi\n", creal(eigenvalues[i]), cimag(eigenvalues[i]));
    }

    // Free memory
    for (int i=0;i<n;i++) {
        free(A[i]);
    }
    free(A);

    return 0;
}

