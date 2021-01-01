# ABC087 - C

n = int(input())
maps = []
maps.append([int(x) for x in input().split()])
maps.append([int(x) for x in input().split()])
ans = 0
temp = 0

# 移動操作が↓か→かの2パターンしかないため、全体での移動パターンも n+2_C_2 程度
# 全探索して、最大値を取るものを出力すればよい

for i in range(n): # ↓移動操作を何回目の移動で行うか
      #print(sum(maps[0][:i+1]),sum(maps[1][i:]))
      temp += sum(maps[0][:i+1]) + sum(maps[1][i:])
      
      if temp > ans:
            ans = temp
      temp = 0
      
print(ans)