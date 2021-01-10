#include <stdio.h>
#include <math.h>

int main(void){
      int temp,n,ans;
      double k = pow(1,2);
      scanf("%d",&n);
    
      while(1){
          k += 1;
          // printf("%f \n",pow(k,2));
          temp = pow(k,2); 
          
          if(temp > n){
                ans = pow(k-1,2);
                printf("%d",ans);
                return 0;
          }
      }
}