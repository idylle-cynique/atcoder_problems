// ABC196 - A

/* 
実装速度を重視して本番中はPythonで書いたが、Cでも実装してみる
Cにmax関数は存在しないため、自分で作る必要があり、ここでは二数のうち大きい方の値を返すmax関数を作成
これを組み合わせて4数のうちの最大値を求めた。max(a-c,max(a-d,max(b-c,b-d)))のようなやり方でもいける
*/

#include <stdio.h>
int max(int a,int b){
    if(a>b){
        return a;
    }else{
        return b;
    }
}
int main(void){
    int a,b,c,d,ans = -100-100;
    
    scanf("%d %d\n%d %d",&a,&b,&c,&d);
    //printf("%d %d %d %d",a,b,c,d);
    
    ans = max(max(a-c,a-d),max(b-c,b-d));
    
    printf("%d",ans);
}