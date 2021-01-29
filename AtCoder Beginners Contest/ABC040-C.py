# ABC040 - C

# https://qiita.com/drken/items/dc53c683d6de8aeacf5a
# ここで解説されているもの。ごく基本的な動的計画法(DP/Dynamic Programming)アルゴリズムの理解が求められる

n = int(input())
a = [int(x) for x in input().split()]
dp = [0]

for i in range(1,n):
      #print(dp); print(a[i],dp[i-2] + abs(a[i]-a[i-2]), dp[i-1] + abs(a[i]-a[i-1]))
      x =  dp[i-1] + abs(a[i]-a[i-1])
      if i != 1:
             x = min(x, dp[i-2] + abs(a[i]-a[i-2]))
      dp.append(x)

print(dp[-1])