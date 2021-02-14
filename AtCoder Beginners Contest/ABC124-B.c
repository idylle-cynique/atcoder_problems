#include <stdio.h>
int main(void){
    int n,h[110],max,ans;
    scanf("%d",&n);
    
    for(int i=0; i<n; i++){
        scanf("%d",&h[i]);
    }
    
    max = 0; ans = 0;
    
    for(int i=0; i<n; i++){
        if(max <= h[i]){
            max = h[i];
            ans++;
        }
    }
    printf("%d",ans);
}