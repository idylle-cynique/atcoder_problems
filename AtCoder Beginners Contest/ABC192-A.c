// 簡単な問題なのでCによる実装とした。
// 100で割ったときの剰余値が0のときがコーナーケースになるので注意

#include <stdio.h>
int main(void){
        int x,ans;
        scanf("%d",&x);
        
        ans = 100-x%100;
        if(ans == 0)
                printf("%d",100);
        else
                printf("%d",ans);
}