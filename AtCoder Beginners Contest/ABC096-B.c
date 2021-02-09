#include <stdio.h>
#include <math.h>
int max(int a,int b,int c){
    if(a>=b && a>=c)
        return a;
    if(b>=c && b>=a)
        return b;
    else
        return c;
}
int main(void){
    // 値が大きいものを二倍した方が当然二倍時の増加値も大きくなるので、一番大きい値を選んでそれをK回二倍すればよい
    int a,b,c,k;
    scanf("%d %d %d\n",&a, &b, &c);
    scanf("%d",&k);
      
    int pow_num = max(a,b,c);
    // printf("%d\n",k);
    printf("%d",(a+b+c-pow_num) + pow_num*(int)pow(2,k));
}