# ARC093 - C

# 基本的には問題で求められているような処理をそのまま実装するだけでよい問題
# ただし、要素数が最大で 10^5個 と非常に大きいので、問題で求められている処理を各要素ごとにその都度行っていると処理が間に合わない
# 各パターンにおける計算処理がほぼ同じであることに着目して
# 全てのスポットに通ったときの合計費用から、あるスポットを飛ばしたときに別途必要になる費用と必要でなくなる費用分だけ計算して
# (通常時の費用総額 - 必要なくなった費用 + 必要になった費用)を出力していけば、その都度最初から計算する必要がなくなり、
# 事前の総額計算にかかる計算量がO(N), Nパターンの実費用計算にかかる計算量もO(N), 全体の計算量もO(N)となり、処理が間に合う

N = int(input())
TouristSpots = [0] + [int(x) for x in input().split()] + [0]
total_costs = 0
#costs = []

for i in range(1,N+2): # 全てのスポットに訪問した時の合計費用を計算
    #costs.append(abs(TouristSpots[i]-TouristSpots[i-1])) # 必要なかったのでコメントアウト
    total_costs += (abs(TouristSpots[i]-TouristSpots[i-1]))

#print(TouristSpots); print(costs); print(total_costs)

for i in range(N): # TouristSpots[i+1]への訪問を取りやめた時の費用を出力
    # 必要なくなった費用を計算
    subtract_cost = (abs(TouristSpots[i]-TouristSpots[i+1]) + abs(TouristSpots[i+1]-TouristSpots[i+2]))
    
    # 別途必要になった費用を計算
    addition_cost = abs(TouristSpots[i+2]-TouristSpots[i])

    # 通常時の費用総額との差し引き分を出力 
    print(total_costs - subtract_cost + addition_cost)
