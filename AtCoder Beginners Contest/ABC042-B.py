# ABC042 - B
n,l = [int(x) for x in input().split()]
s = sorted([input() for x in range(n)])
ans = ""

for i in s:
      ans += i

print(ans)