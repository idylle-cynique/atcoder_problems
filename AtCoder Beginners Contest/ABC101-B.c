#include <stdio.h>
int main(void){
    int n,m,s;
    scanf("%d",&n);
    
    s = 0; m = n;
    
    while(n != 0){
        // printf("%d %d\n",n,s);
        s += (n%10);
        n /= 10;
    }
    
    // printf("%d %d\n",n,s);
    if(m%s == 0)
        printf("Yes");
    else
        printf("No");
}