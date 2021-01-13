# ABC145 - C

# 階乗をそのまま全探索するものだが、最大でも8!= 40320回なので十分高速に解を求めることが出来る
import itertools　# permutations()
import math       # sqrt()

n = int(input())
towns = [[int(x) for x in input().split()] for y in range(n)]
r = list(itertools.permutations([int(x) for x in range(n)],n)) # 有り得る経路のリストを作成
distances = []          # 各ルートにおける移動距離を格納

#print(towns); print(r)

for i in r:                     # 経路のリストを一行ずつ取り出していく
      #print(i)
      temp = 0
      for j in range(len(i)-1): # 取り出した経路リストをもとに実際に距離を計算していく
            #print(i[j],i[j+1]); print(towns[i[j]][0],towns[i[j+1]][0],":",towns[i[j]][1],towns[i[j+1]][1])
            temp += math.sqrt((towns[i[j]][0] - towns[i[j+1]][0])**2 + (towns[i[j]][1] - towns[i[j+1]][1])**2)
      distances.append(temp)

#print(distances)
ans = sum(distances) / len(r)
print(ans)