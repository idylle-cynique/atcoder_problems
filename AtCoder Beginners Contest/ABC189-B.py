# ABC188 - B

n,x = [int(x) for x in input().split()]
total = 0
x *= 100

for i in range(n):
      v,p = [int(x) for x in input().split()]
      total += v*p
      #print(x,total)
      if total > x:
            print(i+1)
            exit()

print(-1)