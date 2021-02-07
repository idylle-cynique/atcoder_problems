// ABC191 - C
#include <stdio.h>
int main(void){
      int v,t,s,d;
      scanf("%d %d %d %d",&v ,&t ,&s ,&d);
      
      if(d < v*t || v*s < d)
            printf("Yes");
      else
            printf("No");
}
