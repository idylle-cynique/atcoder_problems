''' ABC255 - B
    問題文における
        ”すべての人が少なくとも1つの明かりによって照らされるために必要な明かりの強さの最小値”
    という部分を論理展開して上手く解釈することで問題を見通し易くなる

    この文言の通り、全ての人が一つ以上の明かりに照らされている状態を直接的に考えるのではなく
    「最小の明かりの強さで照らした時に、最小数(最低の場合一つ)の明かりにしか照らされない人というのはどういう人なのか」
    というふうに考えてみる。すると
    「明かりを持っている人たちから最も遠い位置にいる人は、最小の明かりの強さでは最小数の明かりの光にしか当たらない」
    ということが分かり、
    「明かりを持つ人たちから最も遠い位置にいる人を照らすことができる明かりの強さの最小値」
    がこの問題における解であることがわかる。

    すると問題の解を求めるにあたっては、
    各人について、明かりを持つ人のうち最も近い位置にいる人との距離を求め、その距離が最も遠い人とのマンハッタン距離を
    三平方の定理と二点間のチェビシェフ距離を用いて表せば、それが最小の明かりの強さとなる
'''

import math

N,K = map(int,input().split())
People = [int(x) for x in input().split()]
coordinates = [[int(x) for x in input().split()] for y in range(N)]
max_dist = 0

for x,y in coordinates:
    min_dist = 10**12
    for i in People:
        idx = i-1
        px,py = coordinates[idx]
        dist = (px-x)**2 + (py-y)**2
        #print("[",x,y,"]","[",px,py,"]",dist)
        min_dist = min(min_dist,dist)
    
    max_dist = max(max_dist,min_dist)

answer = math.sqrt(max_dist)
print(answer)