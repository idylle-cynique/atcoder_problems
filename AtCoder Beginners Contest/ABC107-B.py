# ABC107 - B

# 自力で解けたが、実装にかなり難儀したのでもう一度解いておきたい
# もっとシンプルな実装方法があるはず

h,w  = [int(x) for x in input().split()]
maps = [list(input()) for x in range(h)]
maps_tmp = []

for row in maps:              # 任意の行に入っている値を取り出し、条件を満たすもののみリストに加える
      if row != ["."]*w:
            maps_tmp.append(row)

maps,maps_tmp = maps_tmp,[]

for i in range(len(maps[0])): # 任意の列に入っている値を取り出し、条件を満たすもののみリストに加える
      column = [maps[j][i] for j in range(len(maps))] 
      if column != ["."]*len(maps):
            maps_tmp.append(column)

maps,ans_maps = maps_tmp,[]

for i in range(len(maps[0])): # 前回のループ処理で行と列が反転しているので、もう一度反転させて元に戻す
      column = [maps[j][i] for j in range(len(maps))] 
      ans_maps.append(column)

for i in ans_maps:
      print("".join(i))