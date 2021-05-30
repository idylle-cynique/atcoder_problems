// ABC200 - A
#include <stdio.h>
int main(void){
    int year; scanf("%d",&year);
    
    if (year%100 == 0){
        printf("%d",year/100);
    }else{
        printf("%d",year/100 + 1);
    }
}
