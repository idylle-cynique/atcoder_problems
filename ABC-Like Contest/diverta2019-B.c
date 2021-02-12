// diverta2019 - B

// r,g,bの個数の制約は最大で3000までとあるので、そのままr,g,bを愚直に全探索するとループ回数が大きすぎて処理が間に合わない
// しかし、r,g までの二種類の個数が定まれば 残りの b は探索せずとも、残り必要な個数をbの倍数でまかなえるかを調べさえすればいい
// r,gまでの全探索なら 3000^2 なので 2秒以内での処理が可能

#include <stdio.h>
int main(void){
    int r,g,b,n;
    scanf("%d %d %d %d",&r,&g,&b,&n);
    
    int ans = 0;
    
    for(int i=0; i<=3000; i++){
        for(int j=0; j<=3000; j++){
            if(n-(r*i+g*j) < 0)
                break;
            
            if((n-(r*i+g*j))%b == 0)
                ans ++;    
        }
    }
    printf("%d",ans);
}