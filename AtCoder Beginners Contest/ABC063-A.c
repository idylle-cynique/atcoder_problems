// ABC063 - A
#include <stdio.h>

int main(void){
    int a,b;

    scanf("%d %d",&a,&b);

    if(a+b < 10){
        printf("%d",a+b);
    }else{
        printf("error");
    }
}