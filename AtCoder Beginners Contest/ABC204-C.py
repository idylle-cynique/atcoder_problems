# ABC204 - C

# グラフ探索アルゴリズムの理解と実装を求める問題
# 有向グラフに関する情報が与えられるので、あるノード(節)から出発して到達可能な別のあるノード(節)を選ぶ選び方は何通りあるか、という問題
# 入力されたグラフ情報をもとに隣接リストを生成し、さらにそこから各ノードを出発点としてグラフの探索を行い、
# あるノードではどのノードたちに移動できるかを似たような二次元リストを用いて記録する
# あとは各ノードから到達可能ノードの数を、出発点も含めて足し合わせたものが求められている問題の解となる
# ここではグラフの探索にDFS(深さ優先探索)を用いているが、BFS(幅優先探索)など、他のグラフ探索アルゴリズムを用いてもよい
# なお、グラフの探索には、既に訪問したノードの再訪問によって探索のループが行われてしまわないように、
# なにかしらの形で訪問済みノードのリストを用意し、再訪問が行われないように工夫すること


N,M = map(int,input().split())

ADJ_list = [[] for x in range(N+1)] # 隣接リストのひな型を生成
Reachable_regions = [[] for x in range(N+1)] # 各ノードから出発したときに到達可能なノードを記録

for i in range(M): # 探索に用いる隣接リストを生成
    a,b = map(int,input().split())
    ADJ_list[a].append(b)

def DFS(adj_list,idx): 
    search_stack = [idx]
    reachables = []           # スタート地点となるノードから到達可能なノードの番号を記録
    visited = [False]*(N+1) # 訪問済みノードを記録するリスト False=未訪問 True=訪問済
    visited[idx] = True
    
    while(len(search_stack) != 0):
        v = search_stack.pop() # 探索スタックからノードの情報を得る
        for ele in adj_list[v]:   # 対応するノードに隣接するノードのリストを順番に得る
            if visited[ele] == False: # 未訪問のノードのとき
                search_stack.append(ele) # 次の探索対象として探索スタックにノード番号を加える
                reachables.append(ele)   # 到達可能なノードとしてリストに格納
                visited[ele] = True      # 訪問済みノードとしてリストに記録
    return reachables

def view_2dlist(lst):
    for i in range(len(lst)):
        print(i,":",lst[i])
    return

for i in range(1,N+1):
    tmp = DFS(ADJ_list,i) # DFSを用いて出発点から到達可能な国を探索し、番号リストを得る
    for ele in tmp:       # 二次元リストに格納
        Reachable_regions[i].append(ele)
    
#view_2dlist(Reachable_regions)
ans = 0

for ele in Reachable_regions[1:]:
    ans += (len(ele)+1) # スタート地点とゴール地点が同じでもよい(到達可能なノードのリストに出発したノード自身も含めてよい)のを忘れないこと

print(ans)