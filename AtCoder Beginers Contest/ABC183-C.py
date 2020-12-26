# ABC183 - C

import itertools

n,k = [int(x) for x in input().split()]
t = [[int(x) for x in input().split()] for y in range(n)]
routes = list(itertools.permutations([int(x) for x in range(1,n)]))
ans = 0

for i in range(len(routes)):
      r = [0,0]
      r[1:1] = routes[i]     # 添え字の処理に難儀してしまうので一行ごとに読みだして一次元リストとして処理する
      time = 0
      #print(r)
      
      for i in range(1,len(r)):
            time += t[r[i-1]][r[i]]
      if time == k:
            #print(time,": OK ")
            ans += 1

print(ans)