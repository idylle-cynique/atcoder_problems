// ABC105 - B

#include <stdio.h>
int main(void){
    int n;
    int c,d;
    scanf("%d",&n);
    
    for(c=0; c*7<n; c++){
          for(d=0; d*7<n; d++){
                // printf("cake = %d, donut = %d\n",c,d);
                if(c*7+d*4 == n){
                      printf("Yes");
                      return 0;
                }
          }
    }
    printf("No");
    return 0;
}