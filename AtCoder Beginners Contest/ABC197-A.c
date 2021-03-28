// ABC197 - A
// 基本的な文字列処理の演習にいいので、Cによる提出とした

#include <stdio.h>
int main(void){
    char s[4] = "";
    
    for(int i=0; i<3; i++){
        scanf("%c",&s[i]);
    }
    for(int i=1; i<3; i++){
        printf("%c",s[i]);
    }
    printf("%c",s[0]);
}