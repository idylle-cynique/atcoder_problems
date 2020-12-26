# ABC100 - C

# a_i//2 もしくは a_i*3 のいずれかを行う
# 最終的には、数列中の各要素が2をいくつ約数に持つかを調べ、
# 数列中全体の2の約数数の総和を出力しなさい、と言っているのと等しい？

n = int(input())
a = [int(x) for x in input().split()]
ans = 0

def div2times(x):
      j = 0
      while(x%2 == 0):
            x //= 2
            j += 1
      else:
            return j

for i in range(n):
      ans += div2times(a[i])
      #print(div2times(a[i]))

print(ans)
      
