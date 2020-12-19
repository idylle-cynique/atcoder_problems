# ABC186 - B
h,w = [int(x) for x in input().split()]
b = [[int(x) for x in input().split()] for y in range(h)]
b_min = 100
ans = 0

for i in range(h):
      for j in range(w):
            if b[i][j] < b_min:
                  b_min = b[i][j]
                  
for i in range(h):
      for j in range(w):
            ans += (b[i][j]-b_min)

print(ans)