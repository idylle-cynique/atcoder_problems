// ABC160 - B

// 貪欲法に従い、可能な限り500円硬貨に両替し、残りを可能な限り5円硬貨に両替する
#include <stdio.h>
int main(void){
    int x;
    scanf("%d",&x);
    
    int gladness=0,x_mod=0; // ちゃんと0で初期化しておかないと正しく計算が行われないので注意
    
    gladness += ((x/500)*1000);
    x_mod = x%500;
    gladness += ((x_mod/5)*5);
    printf("%d\n",gladness);
}