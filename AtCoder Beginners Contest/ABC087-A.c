#include <stdio.h>
int main(void){
    int mymoney,cake,donut,ans;
    
    scanf("%d \n %d \n %d",&mymoney,&cake,&donut);
    // printf("%d %d %d",mymoney,cake,donut);
    
    ans = (mymoney-cake)%donut;
    printf("%d",ans);
}