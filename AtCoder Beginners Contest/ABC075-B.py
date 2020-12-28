# ABC075 - B

h,w = [int(x) for x in input().split()]
maps = [input() for x in range(h)]
ex_maps = []

dx = [-1, 0,+1,-1,+1,-1, 0,+1] 
dy = [-1,-1,-1, 0, 0,+1,+1,+1]
      # ↖ ↑ ↗ ← → ↙ ↓ ↘

ex_maps.append(list("."*(w+2)))     # 探索用二次元リストの作成
for i in range(h):
      ex_maps.append(list("." + maps[i] +"."))
ex_maps.append(list("."*(w+2)))

ans_maps = []

for i in range(1,h+1):
      temp = ""
      for j in range(1,w+1):
            cnt = 0
            for k in range(len(dx)):
                  if ex_maps[i][j] == "#":
                        break
                  #print(ex_maps[i+dx[k]][j+dy[k]],k)
                  
                  if ex_maps[i+dx[k]][j+dy[k]] == "#":
                        cnt += 1
                        
            if ex_maps[i][j] == "#":
                  temp += "#"
            else:
                  temp += str(cnt)
      #print(temp)      
      
      ans_maps.append(temp)

for i in ans_maps:
      print(i)
