# ABC094 - C

n = int(input())
x = [int(x) for x in input().split()]
xs = sorted(x)
idx = n//2-1

#print(x); print(xs)
#print(idx,xs[idx])

for i in range(n):
        if x[i] > xs[idx]:
                print(xs[idx])
        else:
                print(xs[idx+1])