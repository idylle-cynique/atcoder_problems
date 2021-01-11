// ABC055 - B
/* 剰余を用いた問題。そのまま愚直に計算を行うと数値が膨大なものになってしまうので、 
   一度の乗算処理ごとに10^9+7(素数)の剰余に直してから計算する。
   (a*b*c)%mod = (a%mod)*(b%mod)*(c%mod) */

#include <stdio.h>
#include <math.h>
int main(void){
    long long int n, i, ans=1;
    long long int mod = pow(10,9)+7;
    scanf("%lld",&n);
      
    for(i=1; i<=n; i++){
            ans *= i;
            ans %= mod;
    }
    printf("%lld",ans);
}