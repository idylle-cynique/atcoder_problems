# ABC153 - C

# HPが大きいモンスターに対して必殺技を使いたい
# 事前にモンスターのHPが大きいものから降順に並べ替えておき、必殺技の使用回数限界まで使う
# あとは各モンスターのHPの総和を求めるだけ

n,k = map(int,input().split())
h = sorted([int(x) for x in input().split()],reverse=True)
ans = 0

for i in h:
    if k > 0:
        k -= 1
        continue
    ans += i

print(ans)  