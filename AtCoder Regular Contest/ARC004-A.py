# ARC004 - A

# 問題で求められている通りに全探索すればよい問題

import math

n = int(input())
fields = [tuple(int(x) for x in input().split()) for y in range(n)]
ans = 0
distance = 0

for i in range(0,n-1):
      for j in range(i,n):
            #print(fields[i],fields[j])
            distance = (fields[i][0]-fields[j][0])**2 + (fields[i][1]-fields[j][1])**2
            
            if ans < distance:
                  ans = distance

print(math.sqrt(ans)) 
    # √a**2 < √b**2 のとき a**2 < b**2 なので、探索時は計算せず最後にmath.sqrt()するだけでもよい
    