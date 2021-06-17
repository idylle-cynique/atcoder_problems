# ABC148 - B

# そのまま要求された通りに実装するだけでよい

n = int(input())
s,t = input().split()
ans = ""

for i in range(n):
    ans += s[i]
    ans += t[i]

print(ans)