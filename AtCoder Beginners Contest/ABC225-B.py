''' ABC225 - B 
    グラフ理論問題
    実際に隣接リストのようなデータ構造をリストを用いて問題の構造を再現し、
    スターの条件を満たすノードが存在するかどうか確認すればよい

    再現だけなら隣接行列などでも再現可能ではあるが、
    頂点数が最大10^5と非常に多いので再現用の二次元リストの探索に
    時間がかかり過ぎてしまう。隣接リストを用いて再現する必要がある
'''

N = int(input())
ADJ_list = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    ADJ_list[a].append(b)
    ADJ_list[b].append(a)

#print(ADJ_list)

for i in range(N):
    #print(len(ADJ_list[i+1]),":",ADJ_list[i+1])
    if len(ADJ_list[i+1]) == N-1:
        print("Yes")
        exit()

print("No")