# ARC025 - A

# 演習としてあえてbit全探索を用いて解く

# 通常想定される解
def normal_answer(d,j):
      ans = 0
      for i in range(7):
            if d[i] > j[i]:
                  ans += d[i]
            else:
                  ans += j[i]
      return ans

ans = 0
d = [int(x) for x in input().split()]
j = [int(x) for x in input().split()]

for a in range(2**7):
      temp = 0
      
      for b in range(7):
            #print((a>>b)&1,end=" ")
            if (a>>b)&1 == 1:
                  temp += d[b]
            else:
                  temp += j[b]
      
      if temp > ans:
            ans = temp
      #print()

print(ans)
#print(normal_answer(d,j))