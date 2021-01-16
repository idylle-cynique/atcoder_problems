#include <stdio.h>
int main(void){
      int k,s, x,y,z;
      int ans = 0;
      
      scanf("%d %d",&k, &s);
      
      for(x=0; x<=k; x++){
            for(y=0; y<=k; y++){
                  // zまで愚直に全探索すると計算量がO(N^3)でCでも到底間に合わなくなる
                  if(x+y <= s && x+y+k >= s){
                        ans ++;
                  }
            }
      }
      printf("%d",ans);
}