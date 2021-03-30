# ABC155 - B

n = int(input())
a = set([int(x) for x in input().split()]) # 重複する値は一度処理すればよいので、set()にして重複要素はまとめる
sieve1 = []
sieve2 = []

for ele in a: # 奇数要素をふるいにかける
    if ele%2 == 0:
        sieve1.append(ele)

for ele in sieve1: # 3,5いずれかの約数である要素をふるいにかける
    if ele%3 == 0 or ele%5 == 0:
        continue
    
    sieve2.append(ele)

#print(sieve1); print(sieve2)