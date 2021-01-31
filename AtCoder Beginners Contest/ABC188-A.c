#include <stdio.h>
#include <stdlib.h>
int main(void){
    int x,y;
    scanf("%d %d",&x, &y);
      
    if(abs(x-y)<3)
        printf("Yes");
    else
        printf("No");
}