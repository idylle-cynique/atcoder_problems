''' ABC252 - B
    与えられた各食品のおいしさ情報のうち、
    おいしさが最大である食品の番号(添え字)を抜き出し、そのリスト内の要素の内、
    そのうち高橋くんが嫌いなものの食品番号リストに含まれる場合にはYes、
    含まれなければNoとすればよい
'''

N,K = map(int,input().split())
Deliciousnesses = [int(x) for x in input().split()]
Dislikes = [int(x) for x in input().split()]

max_delicious = max(Deliciousnesses)
candidates = set()

for n,dish in enumerate(Deliciousnesses):
    if dish == max_delicious:
        candidates.add(n+1)
#print(candidates)

answer = "No"

for number in Dislikes:
    if number in candidates:
        answer = "Yes"
        break

print(answer)