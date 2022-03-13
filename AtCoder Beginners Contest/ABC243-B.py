# ABC243 - B

'''
    A問題と同様入力値の制約を見れば、O(N^2)までの計算量くらいなら許容可能範囲だと分かる
    処理にあたってとくに工夫する必要はなく、至って素直な実装で正答を得ることができる
'''

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ptrn1_cnt = 0
ptrn2_cnt = 0

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                ptrn1_cnt += 1
            else:
                ptrn2_cnt += 1

print(ptrn1_cnt)
print(ptrn2_cnt)