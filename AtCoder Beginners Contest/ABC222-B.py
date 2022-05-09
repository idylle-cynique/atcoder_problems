''' ABC222 - B
    要求されている処理をそのまま実装すればよい
'''

N,P = map(int,input().split())
Scores = [int(x) for x in input().split()]
cnt = 0

for score in Scores:
    if score < P:
        cnt += 1

print(cnt)