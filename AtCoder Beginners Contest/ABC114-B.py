# ABC114 - C
s = list(input())
nums = []
ans = 1000

for i in range(len(s)-2): # 候補リストを作成
      nums.append(int(s[i])*100 + int(s[i+1])*10 + int(s[i+2]))

for n in nums: # もっとも753に近いものを解答として記録
      if ans >= abs(n-753):
            ans = abs(n-753)

print(ans)