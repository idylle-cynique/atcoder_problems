# Code Festival 2017 qual C - B
import itertools

# 全探索による解の導出
# 計算量はO(3^N)だが、数列の要素数は最大でも10個という制約があるので十分処理が間に合う

n = int(input())
a = [int(x) for x in input().split()]
ans = 0
x = list(itertools.product([-1,0,1],repeat=n)) # abs'a_i - b_i| <= 1である数を求めるためのリスト

for i in range(3**n):
      temp = 1
      b = []
      for j in range(n):    # あり得る数列のリストと、リスト内要素の積を求める
            b.append(a[j]+x[i][j])
            temp *= a[j]+x[i][j]
      
      if temp%2 == 0:
            #print(temp,b,end=":"); print("YES")
            ans += 1
            continue
      #print(temp,b,end=":"); print("NO")

print(ans)