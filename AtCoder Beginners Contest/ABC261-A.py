''' ABC261 - A
    問題の処理をそのまま実装するだけでよい
    基本的な解法としてはif文の組み合わせがあるが、分岐がやや複雑になるため
    ここでは問題で求められている数直線をリストを用いて疑似的に再現することで
    チェックするようにした

    当然ながら数直線の長さ分だけのリストが必要となるので計算量の面では問題があり
    if文による実装との間で処理時間に著しい差が出る場合は推奨されない
'''

l,r,L,R = map(int,input().split())
s,g = 0,max(l,r,L,R)
cnt = 0

line = ["" for x in range(g+1)]
for x in range(g+1):
    if l <= x and x <= r:
        line[x] += "R"
    if L <= x and x <= R:
        line[x] += "B"

#print(line)
for x in line:
    if len(x) == 2:
        cnt += 1
    
print(max(cnt-1,0))
