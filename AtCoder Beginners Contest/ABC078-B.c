// ABC067 - B

#include <stdio.h>
int main(void){
    int length,space,interval;
    scanf("%d %d %d",&length,&space,&interval);
    
    int ans = (length-interval)/(space+interval) ; 
            // int型変数の除算は自動的に小数値は切り捨てられる(a//bなどとしなくてよい)
    printf("%d",ans);
    return 0;
}