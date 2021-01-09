// ABC069 - B

#include <stdio.h>
#include <string.h>
int main(void){
      char s[110] = {};
      gets(s);

      printf("%c%d%c",s[0] ,strlen(s)-2, s[strlen(s)-1]);
}