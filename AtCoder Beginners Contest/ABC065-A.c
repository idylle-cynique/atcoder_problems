// ABC065 - A

#include <stdio.h>
int main(void){
    int x,a,b;
    
    scanf("%d%d%d",&x,&a,&b);
    
    if (a >= b){               // 賞味期限前に食べた時
            printf("delicious");
    }else if((a+x) >= b){      // 賞味期限を過ぎたが、X日までに食べた時
            printf("safe");
    }else{                     // 賞味期限後X日を過ぎてから食べた時
            printf("dangerous");
    }
}