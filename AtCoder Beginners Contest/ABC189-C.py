# ABC189- C

# 解説されている通りに実装したものだが、これをPythonで提出してもTLEになる
# トレーシング実行時コンパイルを行ってくれるPyPy3で提出しなくてはいけない

n = int(input())
s = [int(x) for x in input().split()]
x = 0
ans = 0

for l in range(n):
      x = s[l] 
      
      for r in range(l,n):
            x = min(x, s[r])
            ans = max(ans,x*(r-l+1))
            
print(ans)