# ABC016 - C

# 隣接リストを用いて解く問題
# 二次元リストを生成し、インデックスと各番号を対応させてその番号の割り当てられた
# 人物(頂点)と友達(接続)である人物(頂点)の番号を同インデックス列内に格納させる
# あとはある番号の人物の友達として記録された人物の友人リストまで探索し
# {友人の友人関係に含まれる人物}集合 - {自分の直接の友人}集合 - {自分}集合
# で{友達の友達}集合を得るとともに、その集合の長さを出力すればよい

N,M = map(int,input().split())
ADJ_list = [[] for x in range(N+1)]

for i in range(M): # 交友関係を示すグラフデータを隣接リストを用いて格納する
    a,b = map(int,input().split())
    ADJ_list[a].append(b)
    ADJ_list[b].append(a)

ans = []

for i in range(1,N+1): # インデックス0に対応する人物はいないので1～N+1でループさせる

    me = set([i])               # {自分}集合
    friends = set(ADJ_list[i])  # {自分の友達}集合
    friendsfriends = set()      # {自分の友達の友達(自分と共通の友達含む)}集合
    search_list = ADJ_list[i]   # 対応する隣接リストの行を得る
    
    for ele in search_list:     # 自分の友達の番号を得る
        #print(":",ele,ADJ_list[ele])
        for n in ADJ_list[ele]: # 友達の交友リストに入っている番号を{自分の友達の友達}集合に格納
            friendsfriends.add(n)
    #print("ffs:",friendsfriends); print("fs :",friends)
    #print("me :",me); print("rest:",friendsfriends - (friends|me))
    ans.append(len(friendsfriends - friends - me)) # {自分}と{共通の友達}を{友達の友達}集合から差し引き、得た集合の長さを格納

for i in range(len(ans)): # 「友達の友達」の数を格納したansリストを出力
    print(ans[i])