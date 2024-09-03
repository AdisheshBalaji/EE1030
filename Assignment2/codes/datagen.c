#include <stdio.h>
int main(){
	int A[3]={2,-3,4},B[3]={-4,6,8};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=2;i++){

	fprintf(ptr, "%d ",A[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",B[i]);
        }
      
	return 0;
}
