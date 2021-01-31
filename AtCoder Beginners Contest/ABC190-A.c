#include <stdio.h>
int main(void){
    int a,b,c;
    scanf("%d %d %d",&a ,&b ,&c);
    
    if(c == 1)
        b -= 1;
    if(a <= b)
        printf("Aoki");
    else
        printf("Takahashi");
}