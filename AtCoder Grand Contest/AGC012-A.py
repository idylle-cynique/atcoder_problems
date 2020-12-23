# AGC012 - A

# 参加者を昇順にソートし、一番最初の一人と、後ろから2番目までの二人とでチームを組ませていけばどうか？
# そのままの実装の場合TLE(オーダーがO(N^2)？)になってしまったので、
# リストの破壊的な代入処理を用いずに処理を済ませる必要がある

n = int(input())
a = sorted([int(x) for x in input().split()])
ans = 0
i = 1
while(i <= n):
      #print(i-1,(-2*i),(-2*i+1))
      temp = [a[i-1],a[-2*i],a[-2*i+1]]
      ans += temp[1]
      #print(temp)
      i += 1

print(ans)