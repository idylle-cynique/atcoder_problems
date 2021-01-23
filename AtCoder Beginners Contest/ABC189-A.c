// ABC189 - A

#include <stdio.h>
int main(void){
      char a,b,c;
      scanf("%c%c%c",&a,&b,&c);
      
      if(a==b && b==c)
            printf("Won");
      else
            printf("Lost");
}