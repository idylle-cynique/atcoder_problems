# ABC115 - C

n,k = [int(x) for x in input().split()]
h = sorted([int(input()) for x in range(n)],reverse=True)
ans = 10**9

for i in range(n-k+1):
      #print(h[i],h[i+k-1],h[i]-h[i+k-1],ans)
      if h[i]-h[i+k-1] < ans:
            ans = h[i]-h[i+k-1]

print(ans)