# ABC231 - B

# A問題同様、問題文で要求されている処理をそのまま実装すればよい
# Pythonの場合は、collectionsモジュールのCounter()を利用することで容易に実装できる

from collections import Counter

N = int(input())
Votes = [input() for x in range(N)]
Votes_data = Counter(Votes)
#print(Votes_data)    
max_vote = 0
Winner = ""

for name in Votes_data: # 得票数が最大の候補者の名前を取り出す
    #print(name,Votes_data[name])
    if Votes_data[name] > max_vote:
        Winner = name
        max_vote = Votes_data[name]

print(Winner)