#include <stdio.h>
int main(void){
      int n,a;
    
      scanf("%d",&n);  // 支払いたい金額
      scanf("%d",&a);  // 1円玉の枚数
    
      // printf("%d %d \n",n,a);
    
      if ( a >= n%500 )
            printf("Yes");
      else 
            printf("No");
    
}