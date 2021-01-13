// ABC081 - A
#include <stdio.h>
int main(void){
      char m[3] = {};
      int ans=0,i;
      
      scanf("%c%c%c",&m[0],&m[1],&m[2]);
      
      for(i=0; i<3; i++){
            // printf("%c ",m[i]);
            if(m[i] == '1'){
                  ans++;
            }
      }
      printf("%d",ans);
}