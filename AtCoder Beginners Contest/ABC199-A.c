// ABC199 - A

// 要求された通りに実装を行えばよい
#include <stdio.h>
int main(void){
    int a,b,c;
    scanf("%d %d %d",&a, &b, &c);
    
    if(a*a + b*b < c*c){
        printf("Yes");
    }else{
        printf("No");
    }
}
