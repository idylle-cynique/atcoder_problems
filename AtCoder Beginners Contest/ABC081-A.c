/*  ABC081 - A
    問題文で書かれている処理をそのまま実装するだけでよい
*/
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