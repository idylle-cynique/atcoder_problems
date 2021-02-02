h,w = [int(x) for x in input().split()]
meta = [input() for x in range(h)]
grids = ["."*(w+2)]
dx = [  0, +1,  0, -1] # ↑, →, ↓, ←
dy = [ -1,  0, +1,  0] # ↑, →, ↓, ←

for i in meta:    # キャンバスを探索用に調整しておく
      grids.append("." + i + ".")
grids.append("."*(w+2))

#for i in grids:
#　     print(i)
      
for i in range(1,h+1):
      #print(grids[i])
      
      for j in range(1,w+1):
            
            if grids[i][j] == "#":
                  f = False
                  
                  for k in range(len(dx)):
                        #print(grids[i-dy[k]][j-dx[k]],j-dy[k],j-dx[k])
                        if grids[i-dy[k]][j-dx[k]] == "#":
                              f = True
                              break

                  if f == False:
                        print("No")
                        exit()
      
print("Yes")