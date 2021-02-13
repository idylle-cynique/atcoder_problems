# ABC073 - C

n,t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0

for i in range(1,n):
      #print(a[i-1],a[i])
      ans += min(t,a[i]-a[i-1])

print(ans+t)