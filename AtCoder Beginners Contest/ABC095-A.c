// ABC095 - A

#include <stdio.h>
#include <string.h>

int main(void){
    int i,t = 0;
    char s[3] = "";
    scanf("%s",&s);
    
    for(i=0; i<3; i++){
        // printf("%c:o %d\n",s[i],t);
        if(s[i] == 'o'){
            t++;
        }
    }
    printf("%d",700+100*t);
}
