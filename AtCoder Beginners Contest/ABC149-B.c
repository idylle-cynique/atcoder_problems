#include <stdio.h>
int main(void){
    int a=0,b=0,k=0;
    scanf("%d %d %d",&a, &b, &k);
    // printf("%d %d %d\n",a,b,k);
    for(int i=0; i<k; ++i){
        if(a>0)
            a--; continue;
        if(b>0)
            b--; continue;
    }
    printf("%d %d",a ,b);
}
