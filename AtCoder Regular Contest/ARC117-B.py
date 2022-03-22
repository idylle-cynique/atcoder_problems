# ARC117 - B

# まずサンプル問題の出力値や制約から、全探索などによる数え上げではなく、
# ある程度のまとまりをもった形で一括計算が可能である、すくなくとも計算量がO(N)～O(N・logN)程度に収まるものとわかる

N = int(input())
buildings = sorted([int(x) for x in input().split()]) # 数列は処理しやすいように昇順にソートし単調増加数列としておく
arranged_builings = sorted(list(set(buildings)))
ans = (buildings[0]+1)
tmp = buildings[0]
#print(arranged_builings)

for ele in arranged_builings[1:]:
    #print(ans,ele-tmp+1)
    ans *= (ele-tmp+1)
    tmp = ele

#print(arranged_builings) 
print(ans%(10**9+7))