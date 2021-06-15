# ABC205 - B

# 受け取った数列Aとは別に昇順にソートされた1~Nからなる数列Bを生成し
# ソートされた数列Aと整列済み数列Bが等しいかどうか判別すればよい

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in range(1,N+1)]
#print(A); print(B)
if sorted(A) == B:
    print("Yes")
else:
    print("No")