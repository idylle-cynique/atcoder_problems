# ABC185 - D
n,m = [int(x) for x in input().split()]
a = sorted([0] + [int(x) for x in input().split()] + [n+1]) 
a_diff = [a[i+1]-a[i]-1 for i in range(m+1)]    # 白色マスの数を事前に数え上げておく
ans = 0
k = n
#print(a); print(a_diff)

for i in range(m+1):
      if a[i+1]-a[i]-1 < k and a[i+1]-a[i]-1 != 0:
            k = a[i+1]-a[i]-1
#print(k)

for i in range(m+1):
      ans += ((a[i+1]-a[i]-1+(k-1))//k) 
            # k未満のマス余りも1回として数えなくてはいけないので、+(k-1)としておく

print(ans)