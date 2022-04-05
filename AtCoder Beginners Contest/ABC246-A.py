# ABC246 - A

'''
    実際にサンプル入出力値を用いて座標に点をおいてみるとわかるが、
    長方形を描くような4つの座標では4点において
    x座標が同じ点、y座標が同じ点がそれぞれ1つずつ必ず存在する
    つまり、3点の座標の中で、
        - x座標が等しいような点が存在しないx座標値
        - y座標が等しいような点が存在しないy座標値
    を取り出してやれば、それが解となる
'''

from collections import Counter

coordinates_x = []
coordinates_y = []

for _ in range(3):
    x,y = map(int,input().split())
    coordinates_x.append(x)
    coordinates_y.append(y)

cntr_x = Counter(coordinates_x)
cntr_y = Counter(coordinates_y)
#print(cntr_x, cntr_y)

for k,v in cntr_x.items():
    if v%2:
        answer_x = k
for k,v in cntr_y.items():
    if v%2:
        answer_y = k

print(answer_x,answer_y)