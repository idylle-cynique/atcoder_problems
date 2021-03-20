# ABC154 - C

# Pythonの場合は、集合型の重複する値は別個に格納されない、という性質を利用して解くと楽
# 重複する値がある場合、set()に入れたときに、長さがもとの数列リストよりも短くなるので、それを判定条件とする
n = int(input())
a = [int(x) for x in input().split()]
a_set = set(a)

if len(a_set) == n:
        print("YES")
else:
        print("NO")