'''ABC245 - B
    要求されている通りの処理をそのまま実装するだけでよい
'''

N = int(input())
Numbers = set([int(x) for x in input().split()])

for n in range(N+1):
    if n not in Numbers:
        print(n)
        exit()