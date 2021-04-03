# ABC135 - B

# 1回で、という制約があるので特に難しく考える必要はない
# p列とpを昇順に整列したq列を用意し、昇順に整列したい時必ず入れ替え処理を行う必要がある要素の数をチェックすればよい

n = int(input())
p = [int(x) for x in input().split()]
q = sorted(p)
diff = 0
#print(p); print(q)

for i in range(n):
    if p[i] != q[i]:
        diff += 1

if diff <= 2:
    print("YES")
else:
    print("NO")