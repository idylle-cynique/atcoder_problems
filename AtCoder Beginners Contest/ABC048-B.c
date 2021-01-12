// ABC048 - B
// 問題自体は大した内容ではないが、pythonと異なり値の型を意識してコードを書く必要がある
#include <stdio.h>
int main(void){
      long long int a=0,b=0,x=0;          
      scanf("%lld %lld %lld",&a,&b,&x);   
      
      if(a == 0){
            printf("%lld",b/x+1);
            return 0;
      }else{
            printf("%lld",b/x-(a-1)/x);
            return 0;
      }
}
