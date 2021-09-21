# ABC219 - A

# ランクを入力するのではなく、次のランクに至るまでの必要得点を出力する、という点に注意


X = int(input())
ranks = [40,70,90]

for rank in ranks:
    if X < rank:
        print(rank-X)
        exit()

print("expert")