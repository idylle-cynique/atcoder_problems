# ABC187 - B
import itertools

n = int(input())
points = [[int(x) for x in input().split()] for y in range(n)]
ij_list = list(itertools.combinations(points, 2)) # 2点i,jの組み合わせリスト
ans = 0

for k in ij_list: # 二点の傾き m は (y_2-y_1)/(x_2-x_1)
      m = (k[1][1]-k[0][1])/(k[1][0]-k[0][0])
      #print(k,m)
      if -1 <= m and m <= 1:
            ans += 1

print(ans)