// ABC144 - B
#include <stdio.h>
int main(void){
    int kk[81] = {},n,i,j,k=0;
    
    scanf("%d",&n);
    
    for(i=1; i<10; i+=1){
        for(j=i; j<10; j+=1){
            // printf("(%d %d)",i,j);
            kk[k] = i*j;
            k += 1;
        }
    }
    for(i=0; i<81; i+=1){
        if (n == kk[i]){
            printf("Yes");
            return 0;
        }
    }
    printf("No");
}