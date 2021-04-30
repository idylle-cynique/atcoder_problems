# ABC128 - B

# 問題で求められている内容をそのまま実装すればよい問題ではあるが、同じ地域(名)に複数レストランが存在する場合、
# これらを昇順ではなく降順にソートしなくてはならず、通常のソートをそのまま利用するだけでは要求されている処理を実現できない
# 同じ地域内のレストランを別途リストでまとめて、別途キーを指定してソート後reverse()するなど工夫が必要
# ここではソートに利用するキーが数(int)だったので、-1による乗算処理を各要素に対して行い、
# 通常のソートで期待する並びになるようにした

N = int(input())
Restaurants = []
for i in range(N):
    tmp = input().split()
    s,p = tmp[0],int(tmp[1])
    Restaurants.append([s,-1*p,i+1]) # 点数に-1をかけて点の大きい数ほど小さくなるようにする

Restaurants = sorted(Restaurants)

for row in Restaurants: # 整列前の番号を順番に出力していく
    print(row[2])