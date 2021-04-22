# ABC188 - C

# 制約が最大でも2^16 = 65536 と比較的小さいので、そのままトーナメントをシミュレーションするだけでよい
# ただし、解答はレート値ではなく選手番号(初期配列のindex+1)で行う必要があるので注意

n = int(input())
contestants = [int(x) for x in input().split()]
tournament = []

for i in range(2**n): # 選手番号を付与する
    tournament.append((i+1,contestants[i]))

while(len(tournament) != 2): # 決勝戦までシミュレート
    #print(tournament)
    tmp = []
    for i in range(0,len(tournament),2):
        if tournament[i][1] > tournament[i+1][1]:
            tmp.append(tournament[i])
        else:
            tmp.append(tournament[i+1])
    tournament = tmp

#print(tournament)
if tournament[0][1] < tournament[1][1]: # 決勝で負ける(準優勝する)選手の選手番号を出力
    print(tournament[0][0])
else:
    print(tournament[1][0])