#include <stdio.h>
int main(){
	int A[3]={2,-3,4},B[3]={-4,6,-8},C[3]={0,0,0};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=2;i++){

	fprintf(ptr, "%d ",A[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",B[i]);
        }
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",C[i]);
        }
	return 0;
}
