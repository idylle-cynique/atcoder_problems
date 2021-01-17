# ABC156 - B

n,k = [int(x) for x in input().split()]
ans = ""
while(n//k != 0):
      #print(n,n%k)
      ans += str(n%k)
      n //= k

ans += str(n%k)
ans = ans[::-1]

print(len(ans))
