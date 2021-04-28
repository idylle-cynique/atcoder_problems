# ABC199 - B

# 数列Aの要素のうち最大の値～数列Bの要素のうち最小の値が、要求を満たす値となるので
# for文でAの要素から最大値を、Bの要素から最小値を抜き出して(B中の最小値-A中の最大値+1)を解として出力すればよい
# ただしAの要素の最大値がBの要素の最小値を上回ってしまう場合があることに注意し、コーナーケースとして適切に処理すること

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

minimum = 1
maximum = 1000

for i in range(N):
    if A[i] >= minimum: # 数列A の最大値を求める
        minimum = A[i]
    
    if B[i] <= maximum: # 数列B の最小値を求める
        maximum = B[i]


if minimum > maximum: # 数列Aの最大値が数列Bの最小値を上回っている場合、条件を満たす値は存在しない
    print(0)
else:
    print(maximum - minimum + 1)