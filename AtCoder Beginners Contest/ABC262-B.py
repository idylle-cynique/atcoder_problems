''' ABC262 - B
    要求された処理をそのまま実装するだけでよい。
    問題文中で示されている通りに単純無向グラフを基本的なデータ構造(隣接行列もしくは隣接リスト)
    に格納し、それらを三重ループにかけ全ての辺の組み合わせを探索して数え上げていけばよい
    
    制約で示されているように、頂点の数は高々100なので、
    3つの点の頂点をそれぞれ全探索しても(10^2)^3 = 10^6回程度のループで済む
    
    このほか、全探索時の数え上げの際に、並びだけ異なり組み合わせは同じであるものも数え上げられてしまっている
        ex. (1,3,5), (1,5,3), (3,1,5), (3,5,1), (5,1,3), (5,3,1)
    全ての組み合わせに大して3_C_2 = 6通り分の数え上げが行われているので、最後に6で割って解答値を修正している
'''

N,M = map(int,input().split())
ADJ_list = [list() for _ in range(N+1)]
ADJ_set = [set() for _ in range(N+1)]

for i in range(M):
    u,v = map(int,input().split())
    ADJ_list[u].append(v)
    ADJ_list[v].append(u)
    ADJ_set[u].add(v)
    ADJ_set[v].add(u)

cnt = 0

for v1 in range(1,N+1):
    for v2 in ADJ_list[v1]:
        for v3 in ADJ_list[v2]: # この時点でv1-v2-v3までは接続でv3-v1の接続のみ不明
            if v3 in ADJ_list[v1] and len(set([v1,v2,v3])) == 3:
                cnt += 1

answer = cnt//6
print(answer)
            