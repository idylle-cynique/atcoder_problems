// ABC012 - C

#include <stdio.h>
int main(void){
    int total = 0;
    for(int x=1; x<10; x++){
        for(int y=1; y<10; y++){
            // printf("%3d",x*y);
            total += (x*y);
        }// printf("\n");
    }// printf("%d",total);
      
    int n,x;
    scanf("%d",&n);
      
    x = total - n;

    for(int i=1; i<=x; i++){  // 約数の組み合わせを前後の重複を許して指定の形式で出力しろ、ということ
        if(x%i==0 && i<10 &&(x/i)<10){
            printf("%d x %d\n",i ,x/i);
        }
    }
}