# ABC133 - B
import math

# 今一つ問題内容が掴めないが、おそらく問題文通りに実装すれば自ずと答えが求められる性質の問題

n,d = [int(i) for i in input().split()]
x = [[int(i) for i in input().split()] for j in range(n)]
ans = 0

for i in range(n-1):
      temp_1 = x[i]
      for j in range(i+1,n):
            temp_2 = x[j]
            memo = 0
            #print(temp_1,temp_2)
            
            for k in range(d):
                  memo += abs(temp_1[k] - temp_2[k])**2
            
            #print(memo,math.sqrt(memo),int(math.sqrt(memo)))
            if math.sqrt(memo) == int(math.sqrt(memo)):
                  ans += 1

print(ans)