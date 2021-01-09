#include <stdio.h>
#include <string.h>

int main(void){
    int i,s_len;
    char s[100100] = {};
    scanf("%s",s);          // gets()だとよくない？
      
    s_len = strlen(s);      // cだと関数をループ条件式内に書いてはいけない？
      
    for(i=0; i<s_len; i+=1){ 
        // C言語の場合、ループ条件式内にstrlen(s)などのような関数式を書くと大幅に処理効率が低下してしまうらしい
        // pythonと同じ要領で書かないようにすること
        if (i%2 != 1){
              printf("%c",s[i]);
        }
    }
}
