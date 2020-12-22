# ABC098 - B
n = int(input())
s = input()
x = y = set()
ans = 0

for i in range(1,n):
      x,y = set(s[:i]),set(s[i:]) 
            # set化したものの積集合の長さ(要素数)が、問題で求められている
            # "「X と Y のどちらにも含まれている文字」の種類数"にあたる
      temp = x & y
      if len(temp) > ans:
            ans = len(temp)

print(ans)